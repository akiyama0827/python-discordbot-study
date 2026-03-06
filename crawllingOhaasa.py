# 오하아사 웹페이지에서 정보를 크롤링하여 horo_text_list 변수에 저장하는 코드
# horo_text_list는 12*4 사이즈의 2차원 리스트
# 각 별자리별 정보 12열, 1행부터 각각 순위, 별자리명, 설명, 럭키아이템

from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

import os
from dotenv import load_dotenv
load_dotenv()
AUTH_KEY = os.getenv("DEEPL_AUTH_KEY")

import deepl
translator = deepl.Translator(AUTH_KEY)

# 옵션 설정
op = ChromeOptions()
op.add_argument('--headless')
op.add_argument('--no-sandbox')
op.add_argument("window-size=1920x1080")
op.add_argument("disable-gpu")
op.add_argument('--disable-dev-shm-usage')

# Service 객체로 ChromeDriver 경로 지정
service = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=op)

# 테스트: Google 페이지 열기
url = "https://www.asahi.co.jp/ohaasa/week/horoscope/"
driver.get(url)
time.sleep(3)
horo_ul = driver.find_element(By.CLASS_NAME, "oa_horoscope_list")
horo_li = horo_ul.find_elements(By.TAG_NAME, "li")
horo_text_list = []
for horo in horo_li:
    rank = horo.find_element(By.CLASS_NAME, "horo_rank")
    rank_translated = translator.translate_text(rank.text, target_lang="KO")
    title = horo.find_element(By.TAG_NAME, "sapn")
    title_translated = translator.translate_text(title.text, target_lang="KO")
    text = horo.find_element(By.CLASS_NAME, "horo_txt")
    detail = ""
    for i in range(len(text.text.split())-1):
      detail += text.text.split()[i]
    detail_translated = translator.translate_text(detail, target_lang="KO")
    rucky = text.text.split()[-1]
    rucky_translated = translator.translate_text(rucky, target_lang="KO")
    horo_text_list.append([rank_translated.text, title_translated.text, detail_translated.text, rucky_translated.text])
driver.quit()
