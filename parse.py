from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


# 验证文件夹名称    文件夹名称不能含有  / \ : ? " < > |
Regex = re.compile("[/\\\:\*\?\"\<\>\|]")


def clean1(tag,root_url):
    post_fix = tag.a.get("href")
    raw_title = tag.img.get("alt")
    title = Regex.sub("_", raw_title)
    url = urljoin(root_url, post_fix)
    return url, title


def clean2(tag,root_url):
    url = tag.img.get("data-loadsrc") or tag.img.get("src")
    url = urljoin(root_url, url)
    return url


class Parse():
    @classmethod
    def init_spider(cls,s):
        cls.root_url = getattr(s.Config,"root_url")

    @classmethod
    def C_parse_Set(cls,html):
        """
        :param html: html text
        :return: list((url,title)...)
        """
        soup = BeautifulSoup(html,'html.parser')
        temp = soup.select(".cy2-coslist li .showImg")
        kv_info = [clean1(item,cls.root_url) for item in temp]
        return kv_info[3:]

    @classmethod
    def D_parse_Set(cls, html):
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.select(".cy-cosList li div")
        kv_info = [clean1(item, cls.root_url) for item in temp]
        return kv_info

    @classmethod
    def parse_Img(cls,html):
        soup = BeautifulSoup(html,'html.parser')
        temp = soup.select(".tc p")
        info = [clean2(item,cls.root_url) for item in temp]
        return info








