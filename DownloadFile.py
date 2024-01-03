import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/umesh/Upload%20and%20Download.html")
driver.maximize_window()
#Download File
#driver.find_element(By.XPATH,"//*[@id='downloadButton']").click()

#upload File
abc=driver.find_element(By.XPATH,"//*[@id='uploadFile']")
abc.send_keys("C:\\Users\\anjum\\OneDrive\\Desktop\\Anjum_Resume.docx")
