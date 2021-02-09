import requests
from bs4 import BeautifulSoup

base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")

all_p= soup.select("div.article__chunks>div.grid > div.body > p")

for p in all_p:
  print(p.text.replace("\n", " ").strip())