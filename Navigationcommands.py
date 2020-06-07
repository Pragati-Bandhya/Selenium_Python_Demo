from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="D:\Pragati\Python_Selenium\Drivers_Browser\chromedriver_win32\chromedriver")
driver.get("https://www.makemytrip.com/")
time.sleep(10)
print(driver.title)
driver.get("https://appaccess.mphasis.com/")
print(driver.title)

time.sleep(10)
driver.back()
print("Goes back to the previous page"+driver.title)

time.sleep(10)
driver.forward()
print("Goes to the forward page"+driver.title)
time.sleep(10)
driver.refresh()
print("Refreshes the page")
driver.close()
print("CLoses the page")