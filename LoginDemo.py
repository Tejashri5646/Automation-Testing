import time

import click
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)

#driver.get("https://www.youtube.com/")
#driver.minimize_window()
#driver.maximize_window()

#For Moodle Login
driver.get("http://210.212.171.173/login/index.php")
driver.minimize_window()
driver.find_element(By.ID,'username').send_keys(2010039)
driver.find_element(By.ID,'password').send_keys('Anjum@2002')
driver.find_element(By.ID,'loginbtn').click()

driver.find_element(By.XPATH,"//*[@id=loginbtn']").click()


