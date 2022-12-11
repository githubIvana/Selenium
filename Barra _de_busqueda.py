from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tienda.centroestant.com.ar/")

searchbar = driver.find_element(By.ID,"woocommerce-product-search-field-0" )
time.sleep(4)

searchbar.send_keys("Mesada" + Keys.ENTER)
time.sleep(10)

driver.close() 
