from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def Musinsa():          # 무신사 데이터로부터 별점 1점 후기 파싱
    #dataNo = MusinsaData()
    dataNo = ['858911']
    for i in dataNo:
        try:
            driver = webdriver.Chrome("chromedriver")

            driver.get('https://store.musinsa.com/app/goods/'+str(i)+'#estimateBox')
            value = Select(driver.find_element(By.XPATH, '//*[@id="reviewSelectSort"]'))
            value.select_by_visible_text('낮은 평점 순')

            what = Select(driver.find_element(By.XPATH, '//*[@id="reviewGoodsSimilarList"]'))
            what.select_by_visible_text('전체 상품 후기')

            soup = BeautifulSoup(driver.page_source, "html.parser")
            temp = soup.find_all('div', {'class': 'review-list'})

            lev = []
            for i in range(0, 10):
                if temp[i].select("div > span > span > span.review-list__rating__active")[0].get("style") == "width: 20%":
                    lev.append(temp[i].select("div > div.review-contents__text")[0])

            for i in range(len(lev)):
                print(lev[i].text)
        except:
            pass


def MusinsaData():       # 인기순위 데이터
    dataNo = []
    for i in range(1, 10):      # 10개 항목 상의, 아우터, 하의, 가방, ...
        for j in range(1, 6):   # 페이지당 90개 아이템 -> 450 데이터 -> 450 * 10개항목 -> 4500아이템 DataNo.
            driver = webdriver.Chrome(executable_path=r"C:\Users\USER\PycharmProjects\Corona_korea_keep-distance\covid_19_all\chromedriver")

            driver.get('https://search.musinsa.com/category/00'+str(i)+'?d_cat_cd=00'+str(i)+'&brand=&rate=&page_kind=search&list_kind=small&sort=emt_high&sub_sort=&page='+str(j)+'&display_cnt=90&sale_goods=&group_sale=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&shoeSizeOption=&tags=&campaign_id=&timesale_yn=&q=&includeKeywords=&measure=')
            soup = BeautifulSoup(driver.page_source, "html.parser")

            temp = soup.find_all('li', {'class': 'li_box'})

            for t in temp:
                if t.get("data-no") is not None:
                    dataNo.append(t.get("data-no"))
    return dataNo


Musinsa()
