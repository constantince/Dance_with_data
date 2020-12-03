import requests as fetch
from bs4 import BeautifulSoup
import pandas as pd
from base import Base

#setting headrs
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
}
#get html text
html = fetch.get("https://movie.douban.com/top250", headers=headers)

soup = BeautifulSoup(html.text, 'html.parser')

def get_movies_info():
    movies = []
    imgs = soup.select(".item .pic img")
    quotes = soup.select(".item .quote .inq")
    bds = soup.select(".item .info .bd p:nth-of-type(1)")
    stars = soup.select(".item .rating_num")

    for i in range(len(imgs)):
        if(imgs[i] is None or quotes[i] is None or bds[i] is None or stars[i] is None):
            pass
        else:
            item = dict(
                src=imgs[i].get("src"),
                title=imgs[i].get("alt"),
                quote=quotes[i].string,
                bd=bds[i].text.strip().replace('\n', ''),
                star=stars[i].string
            )
            movies.append(item)
    
    return movies

all_movies = get_movies_info()

df = pd.DataFrame(all_movies)

# df.to_csv("./movies3.csv", encoding="utf_8_sig");

