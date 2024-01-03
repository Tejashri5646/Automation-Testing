import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

chkbox=driver.find_element(By.ID,'checkbox1').click()
if chkbox.is_selected():
    pass
else:
    chkbox.click()

chbox =driver.find_element(By.ID,'checkbox2').click()

#Deselecting both chkbox
time.sleep(5)
chkbox.click()
time.sleep(5)
chbox.click()

