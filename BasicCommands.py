from datetime import time

from selenium import webdriver
import time
from selenium.webdriver.common.keys import  Keys

driver=webdriver.Chrome(executable_path="D:\Pragati\Python_Selenium\Drivers_Browser\chromedriver_win32\chromedriver")

driver.get("https://appaccess.mphasis.com/")

print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/h6[1]/a").click()
time.sleep(5)
driver.close()

