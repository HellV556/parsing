import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from fake_useragent import UserAgent

def parser_master():
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Новинки"
    sheet.append(["Название книги", "Автор", "Цена"])

    url = "https://www.chitai-gorod.ru/novelty"
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    level_1 = soup.find("div", class_="app-wrapper")
    level_1_1 = level_1.find("div", class_="app-wrapper__content")
    books = level_1_1.find("div", class_="products-list")

    while books:

        articles = books.find_all("article", class_="product-card product-card product")


        for article in articles:
            price = article.find("div", class_="product-price__value product-price__value--discount")
            if price == None:
                price = article.find("div", class_="product-price__value")
            print(price)
            title = article.find("div", class_="product-title__head").text
            print(title)
            author = article.find("div", class_="product-title__author").text
            print(author)

            sheet.append([title, author, price.text])


        books = books.find_next_sibling("div", class_="products-list")




    workbook.save("books.xlsx")

parser_master()

