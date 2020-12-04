from .base import Base

#https://movie.douban.com/top250?start=
class Douban(Base):
    def __init__(self, save_path):
        # super().__init__(self, {"url":"https://movie.douban.com/top250",  "save_path":save_path});
        self.collections = []
        self.url = "https://movie.douban.com/top250"
        self.save_path = save_path

    #获取对应html节点
    def get_soup_info(self, page):
        soup = self.initial_soup(params=dict(start=page))
        collections = dict(
            lens=len(soup.select(".item .quote .inq")),
            imgs=soup.select(".item .pic img"),
            quotes=soup.select(".item .quote .inq"),
            bds=soup.select(".item .info .bd p:nth-of-type(1)"),
            stars=soup.select(".item .rating_num")
        )
        return collections
    
    #获取所有的节点信息进行存储
    def get_one_page_ino(self, soup_arr):
        for i in range(soup_arr["lens"]):
            item = dict(
                src=soup_arr["imgs"][i].get("src"),
                title=soup_arr["imgs"][i].get("alt"),
                quote=soup_arr["quotes"][i].string,
                bd=soup_arr["bds"][i].text.strip().replace('\n', ''),
                star=soup_arr["stars"][i].string
            )
            self.collections.append(item)
    
    #开始翻页请求
    def page_start(self):
        for p in range(0, 250, 25):
            soup_arr = self.get_soup_info(p)
            self.get_one_page_ino(soup_arr)

        self.save()

    #保存
    def save(self):
        self.save_file()

    def make(self):
        print("make it now...")


# if __name__ == "__main__":
#     print("douban.py")
    