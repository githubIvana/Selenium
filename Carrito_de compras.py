from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()  #esto es para borrar todas las cookies
driver.maximize_window()  #para ampliar el tamano de la ventana completa.

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


time.sleep(2)
 
actions = ActionChains(driver)

muebles = driver.find_element(By.LINK_TEXT,"Muebles")

time.sleep(4)  

actions.move_to_element(muebles).perform()

bibliotecas = driver.find_element(By.LINK_TEXT, "Bibliotecas")

actions.move_to_element (bibliotecas).click().perform()

time.sleep(5)


product = driver.find_element(By.LINK_TEXT,"Biblioteca 6001")
product.click() 
tituloproducto=driver.find_element(By.XPATH,("//*[@id='product-14045']/div/div[1]/div/div[2]/div[4]/span[1]/span")).text

if "6001"==tituloproducto:
    print("Validar que se redireccionó a la pagina del producto elegido: PASS" )
else:
    print("Validar que se redireccionó a la pagina del producto elegido: FAIL" )
    error+=1


time.sleep(5)

Boton_anadir = driver.find_element(By.XPATH,"//*[@id='product-14045']/div/div[1]/div/div[2]/form/div/div/div[2]/div/div/button")
Boton_anadir.click()

time.sleep(3)
cancarrito = driver.find_element(By.XPATH,"//*[@id='masthead']/div[1]/div[4]/ul/li[3]/div/a/i").get_attribute("data-icon-label")

time.sleep(6)

if int(cancarrito) > 0:
    print("Validar que el producto se agrego al carrito: PASS")
else:
    print("Validar que el producto se agrego al carrito: FAIL")
    error+=1
print("")
if error==0:
    print("Test case Funcionamiento del botón 'Añadir al carrito' : PASS")
else:
    print("Test case Funcionamiento del botón 'Añadir al carrito' : FAIL")

driver.close() 