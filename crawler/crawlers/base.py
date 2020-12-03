import requests as fetch
from bs4 import BeautifulSoup
import pandas as pd

class Base(object):
    def __init__(slef, url, save_path):
        self.collections = []
        self.url = url
        self.save_path = save_path
    
    def save_file(self):
        df = pd.DataFrame(self.collections)
        df.to_csv(self.save_file)

    def initial_soup(self, params):
        html = fetch.get(self.url + '')
        return BeautifulSoup(html.text, "html.parser")
