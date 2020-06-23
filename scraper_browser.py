import os

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

PROJECT_ROOT = os.path.abspath(os.path.dirname('selenium_method.py'))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
driver = webdriver.Chrome(executable_path=DRIVER_BIN)
games = set()

url = 'https://store.steampowered.com/search/'

driver.get(url)

SCROLL_PAUSE_TIME = 5

last_height = driver.execute_script("return document.body.scrollHeight")

f = open("steam_data.txt", "w", encoding="utf-8")
f.write("")
f.close()
for x in range(720):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    last_height = new_height
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    t = soup.find_all('a', class_="search_result_row ds_collapse_flag")
    f = open("steam_data.txt", "a", encoding="utf-8")
    for line in t:
        try:
            if line['data-ds-appid'] not in games:
                games.add(line['data-ds-appid'])
                print(line['data-ds-appid'])
                print(line.find('span').string)
                f.write(line['data-ds-appid'] + "," + line.find('span').string + "\n")
        except:
            print("Missing Data Skipping...")
    f.close()
