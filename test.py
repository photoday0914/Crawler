import requests
import re
from bs4 import BeautifulSoup

url = "https://medium.com/"

res = requests.get(url)
res.raise_for_status()
# soup1 = BeautifulSoup(res.text)
soup = BeautifulSoup(res.text, "lxml")
# f = open("res.txt", "w", encoding="utf-8-sig")
# f1 = open("res1.txt", "w", encoding="utf-8-sig")
# f.write(soup.prettify())
# f1.write(soup1.prettify())
# print(soup)
posts = soup.find_all("h2", attrs={"class":"bv he ec bx ct it im in iu ip ir fk by"})
for i in range(0, len(posts)):
    print(str(i) + ':' + posts[i].get_text())
