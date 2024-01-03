import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)

driver.get("https://testautomationpractice.blogspot.com/")
#act=ActionChains(driver)
driver.maximize_window()

#Screenshot Methods
#save_screenshot
#get_

driver.save_screenshot("C:\\Users\\anjum\\OneDrive\\Desktop\\ScreenshotD\\automation.jpeg")
