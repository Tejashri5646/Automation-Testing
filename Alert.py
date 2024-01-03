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
driver.maximize_window()

# driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button[1]').click()
# ab=driver.switch_to.alert
# time.sleep(5)
# ab.accept()

#Scroollbar
driver.execute_script("window.scrollbarBy(0,800)","")
#driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button[1]').click()