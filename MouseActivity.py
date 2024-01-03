#
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
act=ActionChains(driver)
driver.maximize_window()

time.sleep(3)
driver.execute_script("window.scrollBy(0,200)","")

menu=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
#act.double_click(menu).perform()

#Right Click
act.context_click(menu).perform()

