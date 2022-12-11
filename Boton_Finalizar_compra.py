from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 
import time

driver = webdriver.Chrome()
driver.delete_all_cookies()
driver.maximize_window()
driver.get("https://tienda.centroestant.com.ar/")

time.sleep(3)

acceso = driver.find_element(By.LINK_TEXT,"Acceder")
acceso.click()

time.sleep(3)

usuario = driver.find_element(By.ID,"username")
usuario.send_keys("ivanadelvalleportela1987@hotmail.com" + Keys.TAB)

time.sleep(3)

password = driver.find_element(By.ID,"password")
password.send_keys("Ratarata2684"  + Keys.ENTER)

time.sleep(3)

actions = ActionChains(driver)

Mi_carrito = driver.find_element(By.LINK_TEXT,"Mi Carrito")

actions.move_to_element(Mi_carrito).perform()

boton_finalizar_compra = driver.find_element(By.LINK_TEXT,"Finalizar compra")
boton_finalizar_compra.click()

time.sleep(4)

driver.close()
