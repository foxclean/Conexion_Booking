#------------- Inician Imports. -------------#
#import urllib
#import utllib.request
import re
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import random
import datetime
import os
#----
import pymssql
import _mssql
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#------------- Finalizan Imports. -------------#
#------------- Inicia Declaración de Variables Globales. -------------#
#------------- Inicia Configuración de BD. -------------#
#--- Variables de conexión a la base de datos.
connection = pymssql.connect(server='66.232.22.196',
                            user='FOXCLEA_TAREAS',
                            password='JACINTO2014',
                            database='FOXCLEA_TAREAS'
                            #charset='utf8mb4',
                            #cursorclass=pymssql.cursors.DictCursor
                           )
#---
#------------- Finaliza Configuración de BD. -------------#
#--- Navegador.
#file_path = os.path.join(sys.path[0]) + "\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe"
file_path = os.path.join(sys.path[0]) + "\geckodriver.exe"
binary = FirefoxBinary(file_path)
print(file_path)
driver = webdriver.Firefox()

#driver = webdriver.PhantomJS(file_path) #<--- Se especifica el path del exe.
# driver.set_page_load_timeout(240)
#--- BD
#---- Funcion General para filtrar contenido.
def get_content(selector, filters):
    #---
    return [t.get_text() for t in filters.select(selector)] #<--- Se Devuelven los datos Filtrados.
#---
AUTH_DATA_CHECK = ['Gloria','Figueras','+34620087298','10','29','72']
URL_1 = 'https://admin.booking.com/'

driver.get(URL_1)
innerHTML = driver.execute_script("return document.body.innerHTML")

#----
select = Select(driver.find_element(By.CSS_SELECTOR, ".section-login .form-group select"))
select.select_by_value('es')
time.sleep(5)
# find the element that's name attribute is q (the google search box)
inputMail = driver.find_element_by_id("loginname")
inputPass = driver.find_element_by_id("password")
#-------
# type in the search
inputMail.send_keys("USUROM2")
inputPass.send_keys("Roma2017")


# submit the form (although google automatically searches now without submitting)
inputMail.submit()

time.sleep(15)
#-----
option = driver.find_element_by_link_text('Anfitrión')
option.click()
time.sleep(1)
#-----
"""
menu = driver.find_element_by_link_text('Anuncios')
menu.click()
menu.click()"""
time.sleep(3)
URL_2 = "https://www.airbnb.es/rooms/"
driver.get(URL_2)
innerHTML = driver.execute_script("return document.body.innerHTML")

page_data = (BeautifulSoup(innerHTML, "html.parser"))
#---
calendar_link = []
for g_link in page_data.select(".listing div .space-top-4 a"):
    temp_link = g_link.get('href')
    #f_link = temp_link.split('?')
    #last_link = str(PORTAL[2]) + str(f_link[0])
    if ('calendar' in temp_link):
        calendar_link.append(temp_link)
print('--------')
print(calendar_link)
print('--------')
print(calendar_link[0])
driver.get(calendar_link[0])
time.sleep(5)
select = Select(driver.find_element(By.CSS_SELECTOR, ".calendar-month .calendar-month__dropdown div select"))
select.select_by_value('2017-11')
time.sleep(5)
#""
#-----
days = driver.find_elements(By.CSS_SELECTOR, ".container_e296pg div .days-container .list-unstyled .tile")
time.sleep(5)

for x in range(0,len(days)):    
    text = days[x].text
    text_split = text.split('\n')
    print('Completo ', text_split)
    print('Día ', text_split[0])
    day = text_split[0]
    #---
    if (len(text_split[0]) > 2):
        temp_day = re.findall('\d+', text_split[0])
        day = temp_day[0]
        print(day)
    #--- 
    if(int(day) == 20):
        days[x].click()

time.sleep(1)

#-- Valor Original 95

inputPrice = driver.find_element(By.CSS_SELECTOR, ".panel-body span .space-1 div .col-sm-6 input.undefined")
# Clean the input
inputPrice.clear()
# type in the search
inputPrice.send_keys(150)
# submit the form (although google automatically searches now without submitting)
inputPrice.submit()