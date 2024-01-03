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
#var1=driver.find_element(By.ID,'radio2').click()
var=driver.find_element(By.ID,'radio1')
if var.is_selected():
    pass
else:
    var.click()

time.sleep(5)
driver.find_element(By.ID,'radio2').click()

