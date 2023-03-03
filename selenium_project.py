from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://medium.com"
browser.get(url)

import time
interval = 2

# prev_height = browser.execute_script("return document.body.scrollHeight")

for i in range(1, 3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    # curr_height = browser.execute_script("return document.body.scrollHeight")
print("scroll done!")

soup = BeautifulSoup(browser.page_source, "lxml")
divs = soup.find_all("div", attrs={"class":"ae cx"})

f = open("list.txt", "w", encoding="utf-8-sig")
count = 1
for div in divs:
    post = div.find("h2")
    f.write(str(count) + '\t' + post.get_text() + "\n")
    count = count + 1