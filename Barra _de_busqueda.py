from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
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

searchbar = driver.find_element(By.ID,"woocommerce-product-search-field-0" )
time.sleep(4)

searchbar.send_keys("Mesada" + Keys.ENTER)

time.sleep(8)

camposearch= driver.find_element(By.XPATH,"//*[@id='masthead']/div[1]/div[3]/ul/li/div/div/form/div[1]/div[1]/label").text
if "Buscar por:"==camposearch:
    print("validar visualizacion campo 'Barra de busqueda': PASS")
else:
    print("validar visualizacion campo 'Barra de busqueda': FAIL")
    error+=1
 
iconbusqueda= driver.find_element(By.XPATH,"//*[@id='masthead']/div[1]/div[3]/ul/li/div/div/form/div[1]/div[2]/button/i").text
if ""==iconbusqueda:
    print("validar visualizacion boton icono de busqueda : PASS")
else:
    print("validar visualizacion boton icono de busqueda : FAIL")
    error+=1

print("")
if error==0:
    print("Test case Funcionamiento 'Barra de busqueda' : PASS")
else:
    print("Test case Funcionamiento 'Barra de busqueda' : FAIL")


driver.close() 
