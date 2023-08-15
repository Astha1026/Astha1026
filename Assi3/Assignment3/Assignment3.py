# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()


driver.get("https://www.amazon.ca")
time.sleep(3)


search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("handbags women")

search_bar.send_keys(Keys.RETURN)


time.sleep(5)

assert "handbags women" in driver.title


handbags_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div/div[1]/div/span/a/div")

handbags_link.click()


time.sleep(5)


add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()

time.sleep(5)



proceed_to_checkout_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[3]/div[5]/div/div[1]/div[1]/div/form/div/div[3]/span/span/span/input")
proceed_to_checkout_link.click()
time.sleep(2)

go_to_cart_button = driver.find_element("id","sw-gtc_CONTENT")
go_to_cart_button.click()
time.sleep(5)




driver.close()
