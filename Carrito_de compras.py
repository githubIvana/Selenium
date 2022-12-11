from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time

driver = webdriver.Chrome()
driver.delete_all_cookies()  #esto es para borrar todas las cookies
driver.maximize_window()  #para ampliar el tamano de la ventana completa.

driver.get("https://tienda.centroestant.com.ar/")

time.sleep(2)
 
actions = ActionChains(driver)

muebles = driver.find_element(By.LINK_TEXT,"Muebles")

time.sleep(4)  #hasta aca funcionó

actions.move_to_element(muebles).perform()

bibliotecas = driver.find_element(By.LINK_TEXT, "Bibliotecas")

actions.move_to_element (bibliotecas).click().perform()

time.sleep(5)


product = driver.find_element(By.LINK_TEXT,"Biblioteca 6001")
product.click() 


time.sleep(5)

Boton_anadir = driver.find_element(By.XPATH,"//*[@id='product-14045']/div/div[1]/div/div[2]/form/div/div/div[2]/div/div/button")
Boton_anadir.click()

time.sleep(6)

driver.close() 