from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd

driver = webdriver.Chrome(executable_path="chromedriver.exe")

products = []
prices = []

driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

content = driver.page_source

#print(content)

parsed_content = bs(content, "html.parser")

for eachproduct in parsed_content.findAll("a", href=True, attrs={"class": "_1fQZEK"}):
	name = eachproduct.find("div", attrs={"class": "_4rR01T"})
	price = eachproduct.find("div", attrs={"class": "_30jeq3 _1_WHN1"})
	products.append(name.text)
	prices.append(price.text)

print(products)
print(prices)
df = pd.DataFrame({"Product": products, "Prices": prices})
df.to_csv("laptops.csv", index=False, encoding='utf-8')
	