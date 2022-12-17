from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()
driver.maximize_window()
driver.get("https://tienda.centroestant.com.ar/")
error=0

time.sleep(5)

acceso = driver.find_element(By.LINK_TEXT,"Acceder")
textoacceso= driver.find_element(By.XPATH,"//*[@id='top-bar']/div/div[3]/ul/li[2]/a/span").text
if "Acceder"==textoacceso:
    print("validar visualizacion de link 'Acceder': PASS")
else:
    print("validar visualizacion de link 'Acceder': FAIL")
    error+=1

acceso.click()

time.sleep(5)

usuario = driver.find_element(By.ID,"username")
usuario.send_keys("ivanadelvalleportela1987@hotmail.com" + Keys.TAB)

time.sleep(5)

password = driver.find_element(By.ID,"password")
password.send_keys("Ratarata2684"  + Keys.ENTER)

time.sleep(5)


actions = ActionChains(driver)

Mi_carrito = driver.find_element(By.LINK_TEXT,"Mi Carrito")

actions.move_to_element(Mi_carrito).perform()

textomi_carrito= driver.find_element(By.XPATH,"//*[@id='masthead']/div[1]/div[4]/ul/li[3]/div/a/span").text
if "Mi Carrito"==textomi_carrito:
    print("validar visualizacion de boton 'Mi carrito': PASS")
else:
    print("validar visualizacion de boton 'Mi carrito': FAIL")
    error+=1

boton_finalizar_compra = driver.find_element(By.LINK_TEXT,"Finalizar compra")
textfinalizar_compra= driver.find_element(By.XPATH,"//*[@id='masthead']/div[1]/div[4]/ul/li[3]/ul/li/div/p[2]/a[2]").text
if "Finalizar compra"==textfinalizar_compra:
    print("validar que se visualice boton 'Finalizar compra': PASS")
else:
    print("validar que se visualice boton 'Finalizar compra': FAIL")
    error+=1

print("")
if error==0:
    print("Test case Funcionamiento del botón 'Finalizar compra' : PASS")
else:
    print("Test case Funcionamiento del botón 'Finalizar compra' : FAIL")

boton_finalizar_compra.click()



time.sleep(4)

driver.close()
