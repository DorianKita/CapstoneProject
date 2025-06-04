import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import lxml

FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSfTzJL9kXncq0imbiFtyiY4GFEBhI7FGyy30gVc3B2TEfpVLg/viewform?usp=header'
SITE_LINK = 'https://appbrewery.github.io/Zillow-Clone/'

page = requests.get(SITE_LINK)
soup = BeautifulSoup(page.text, "lxml")

list_of_addresses = []
list_of_links = []
list_of_prices = []

addresses = soup.find_all('address')

for address in addresses:
    list_of_addresses.append(address.text.strip().replace('|',','))

for link in soup.find_all(class_='StyledPropertyCardDataArea-anchor'):
    list_of_links.append(link.get('href'))

for price in soup.find_all(class_='PropertyCardWrapper__StyledPriceLine'):
    price_text = price.text[0:6]
    list_of_prices.append(price_text)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)



for num in range(len(list_of_prices)):
    driver.get(FORM_LINK)
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').click()
    driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(list_of_addresses[num])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').click()
    driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(list_of_prices[num])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').click()
    driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(list_of_links[num])
    driver.find_element(By.CLASS_NAME, 'uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd').click()

    # time.sleep(1)

    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfTzJL9kXncq0imbiFtyiY4GFEBhI7FGyy30gVc3B2TEfpVLg/formResponse')
    # time.sleep(1)
    driver.find_element(By.TAG_NAME, 'a').click()
    # time.sleep(1)

