from .base import Base as Crawlers

class Douban(Crawlers):
    def __init__(slef, url, save_path):
        self.collections = []
        self.url = url
        self.save_path = save_path

    #获取对应html节点
    def get_soup_info(self, page):
        soup = super.initial_soup(page=page)
        return [
            soup.select(".item .pic img"),
            quotes = soup.select(".item .quote .inq"),
            bds = soup.select(".item .info .bd p:nth-of-type(1)"),
            stars = soup.select(".item .rating_num")
        ]
    #获取所有的节点信息进行存储
    def get_one_page_ino(self, soup_arr):
        for i in range(len(soup_arr)):
             item = dict(
                src=imgs[i].get("src"),
                title=imgs[i].get("alt"),
                quote=quotes[i].string,
                bd=bds[i].text.strip().replace('\n', ''),
                star=stars[i].string
            )
            self.collections.append(item)
    #开始翻页请求
    def page_start(self):
        for p in range(0, 10, 25):
            soup_arr = self.get_soup_info(p)
            self.get_one_page_ino(soup_arr)

        self.save()
    #保存
    def save():
        super.save_file()
