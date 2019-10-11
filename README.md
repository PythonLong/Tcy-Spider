# Tcy-Spider

## 介绍

**爬取[推次元](https://t2cy.com/)网址图片资源** ![详细](https://t2cy.com/skin/default/images/favicon.ico)

目前仅支持 **"Cos"  "日常"** 2个栏目

当前为同步爬取


**TODO**
- [ ] IP代理池
- [ ] 异步多 线程/进程 加快效率


## 开始

### 配置文件的使用方法

配置文件为 config.json 如下:
```
    {
        # 爬取的栏目 值为 cos or daily 
        # 不填、填错 默认为 cos
        "type" : "cos",

        # 保存的目录
        "save_path":"D:\\TcySet\\Cos_end",

        # 起始 结束页面 注意:前开后开 如:1-5(含5)
        "start":1,
        "end":5
    }
```
