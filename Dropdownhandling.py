import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

drp=Select(driver.find_element(By.ID,'drop1'))
#select by visible test
#drp.select_by_visible_text("doc 1")
#drp.select_by_index(2)
drp.select_by_value("jkl")
