import os
import requests
import random
import time
from requests.exceptions import Timeout
from parse import Parse
from setting import Config


class Spider():
    def requests(self,url,**kwargs):
        headers = {
            "User_Agent":random.choice(self.Config.User_Agent)
        }
        response = requests.get(url,headers=headers,**kwargs)
        response.encoding = "utf8"

        return response

    def config_from_object(self,obj):
        self.Config = obj

    def DirExsit(self,name):
        """
        if dir not exist make it
        :param name:
        :return: abs_dir
        """
        dir_path = os.path.join(self.Config.save_path,name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            return dir_path
        return False

    def get_imgSet_list(self,url):
        response = self.requests(url)
        if self.Config.type != "cos":
            Set_List = Parse.D_parse_Set(response.text)
        else:
            Set_List = Parse.C_parse_Set(response.text)
        return Set_List

    def get_imgSet(self,Set_list):
        for Set_url,title in Set_list:
            dir_path = self.DirExsit(title)
            if not dir_path:
                continue
            response = self.requests(Set_url)
            Img_List = Parse.parse_Img(response.text)
            total = len(Img_List)
            print(title,"Downloading...")
            for i,item_Img in enumerate(Img_List,1):
                try:
                    self.down_load(item_Img,dir_path,i,total)
                except OSError:
                    print("Error  url:{}  Parse_result:{} Continue next".format(Set_url, Img_List))
                    break
                time.sleep(random.random())
            time.sleep(random.randint(3,8))

    def down_load(self,url,dir,current,total):
        try:
            response = self.requests(url)
        except Timeout:
            print("Fail {}/{} Time_out".format(current, total))
            return

        if response.status_code != 200:
            print("Fail {}/{} State_error".format(current, total))
        post_fix = str(current) + url[-4:]
        name = os.path.join(dir,post_fix)
        with open(name,"wb") as f:
            f.write(response.content)

        print("\tCess {}/{}".format(current, total))


    def run(self):
        for num in range(self.Config.start,self.Config.end + 1):
            url = self.Config.root_url
            if num != 1:
                url = "{}/index_{}.html".format(self.Config.root_url,num)
            Set_List = self.get_imgSet_list(url)
            self.get_imgSet(Set_List)
            time.sleep(random.randint(3,8))

        print("\t\tRun finish!")

def create_spider():
    s = Spider()
    Config.init()
    s.config_from_object(Config)
    Parse.init_spider(s)

    return s

if __name__ == '__main__':
    pass

