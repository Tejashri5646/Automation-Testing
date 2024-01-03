import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
# driver.get("http://brightinfo.in/umesh/index1.html")
# #minimize window
# driver.minimize_window()
# print(driver.title)

#time.sleep(5)

# driver.get("https://www.youtube.com/")
# print(driver.title)

#driver.back()
#time.sleep(5)
#driver.forward()
r
time.sleep(5)
driver.get("http://210.212.171.173/login/index.php")
driver.minimize_window()
driver.find_element(By.ID,'username').send_keys(2010039)
driver.find_element(By.ID,'password').send_keys('Anjum@2002')
driver.find_element(By.ID,'loginbtn').click()
