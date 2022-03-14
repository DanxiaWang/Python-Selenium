'''
Created on Dec 5, 2021

@author: Danxia Wang
'''

# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sqlite3
'''
Create ProductInfo data frame
'''
conn = sqlite3.connect('BestBuyPrinters.db')
c = conn.cursor()

# Get BestBuy webpage
driver=webdriver.Chrome()
driver.get("https://www.bestbuy.com/")

# Close pop window
button=driver.find_element(By.CLASS_NAME, "c-close-icon.c-modal-close-icon")
try:
    button.click()
except:
    pass

# Pages URL
product_list_URL_pattern_str="https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&browsedCategory=pcmcat266500050030&cp=$NUM$&id=pcat17071&iht=n&ks=960&list=y&sc=Global&st=categoryid%24pcmcat266500050030&type=page&usc=All%20Categories"

# Get product information

for k in range(12):
    driver.get(product_list_URL_pattern_str.replace("$NUM$",str(k+1)))
    titles=driver.find_elements(By.XPATH,"//div[@class=\"shop-sku-list-item\"]//*[@class=\"sku-title\"]")
    models=driver.find_elements(By.XPATH, "//div[@class=\"shop-sku-list-item\"]//*[@class=\"sku-model\"]/div[1]/span[2]")
    SKUs=driver.find_elements(By.XPATH, "//div[@class=\"shop-sku-list-item\"]//*[@class=\"sku-model\"]/div[2]/span[2]")
    prices=driver.find_elements(By.XPATH, "//div[@class=\"shop-sku-list-item\"]//*[@class=\"priceView-hero-price priceView-customer-price\"]/span[1]")
    reviews=driver.find_elements(By.XPATH, "//div[@class=\"shop-sku-list-item\"]//*[@class=\"c-reviews-v4 c-reviews order-2\"]")
    stars=driver.find_elements(By.XPATH, "//div[@class=\"shop-sku-list-item\"]//*[@class=\"visually-hidden\"]")
    for i in range(len(titles)):       
        ProductName= titles[i].text
        Brand= titles[i].text.split()[0]
        Model=models[i].text
        SKU=SKUs[i].text
        Price=prices[i].text
        Stars = stars[i].text.split()[2]
        TotalReviews = reviews[i].text.strip("()")
        c.execute('''INSERT INTO ProductInfo(ProductName,Brand,Model,SKU,Price,Stars,TotalReviews) VALUES(?,?,?,?,?,?,?)''', (ProductName,Brand,Model,SKU,Price,Stars,TotalReviews))
        conn.commit()
conn.close()

#Printers_data.to_excel("Printers_data.xlsx", index=False)

