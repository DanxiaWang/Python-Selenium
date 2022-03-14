# Imports
'''
Created on Dec 5, 2021

@author: Danxia Wang
'''

import time
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By


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
# All pages URL pattern
product_list_URL_pattern_str="https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&browsedCategory=pcmcat266500050030&cp=$NUM$&id=pcat17071&iht=n&ks=960&list=y&sc=Global&st=categoryid%24pcmcat266500050030&type=page&usc=All%20Categories"
# Page URL list
plinks=[]
for k in range(5):
    driver.get(product_list_URL_pattern_str.replace("$NUM$",str(k+1)))
    productlinks=driver.find_elements(By.XPATH, "//div[@class=\"shop-sku-list-item\"]//*[@class=\"sku-title\"]/h4/a")    
    for plink in productlinks:
        plink=plink.get_attribute('href')
        plinks.append(plink)
for p in range(len(plinks)):  
    page=driver.get(plinks[p])
    try:
        close=driver.find_element(By.ID, "survey_invite_no").click()
    except:
        pass    
    reviews=driver.find_element(By.PARTIAL_LINK_TEXT,"Reviews").click()   
    try:
        allreviews=driver.find_element(By.XPATH, "//div[@class=\"see-all-reviews-button-container\"]/a").click()    
    except:
        pass
    SKU=driver.find_element(By.XPATH, "//dl[@class=\"model-and-sku body-copy-lg\"]/dd[3]").text
    customer_names=driver.find_elements(By.XPATH, "//div[@class=\"review-item-header d-none d-md-block col-md-4 col-lg-3\"]//*[@class=\"ugc-author v-fw-medium body-copy-lg\"]/strong")
    stars=driver.find_elements(By.XPATH, "//div[@class=\"review-rating\"]/div/p")
    review_titles=driver.find_elements(By.XPATH, "//h4[@class=\"c-section-title review-title heading-5 v-fw-medium\"]")
    reviews=driver.find_elements(By.XPATH, "//div[@class=\"ugc-review-body body-copy-lg\"]/p")
    dates=driver.find_elements(By.XPATH, "//time[@class=\"submission-date\"]")
    for i in range(len(customer_names)):
        CustomerName = customer_names[i].text
        Star = stars[i].text.split()[1]
        Keyword = review_titles[i].text
        Reviews = reviews[i].text
        ReviewDate = dates[i].text
        c.execute('''INSERT INTO CustomerReviews(SKU,CustomerName,Star,Keyword,Reviews,ReviewDate) VALUES(?,?,?,?,?,?)''', (SKU,CustomerName,Star,Keyword,Reviews,ReviewDate))
        conn.commit()      
    continue
conn.close()
        

