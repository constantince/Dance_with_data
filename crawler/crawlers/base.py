import requests as fetch
from bs4 import BeautifulSoup
import pandas as pd

class Base(object):
    #初始化部分信息
    def __init__(slef, url, save_path):
        self.collections = []
        self.url = url
        self.save_path = save_path
    #保存文件
    def save_file(self):
        df = pd.DataFrame(self.collections)
        df.to_csv(self.save_file, encoding="utf_8_sig")
    #初始化html对象
    def initial_soup(self, params):
        #setting headrs
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
        }
        #发送请求
        html = fetch.get(self.url + params=params)
        return BeautifulSoup(html.text, "html.parser")
