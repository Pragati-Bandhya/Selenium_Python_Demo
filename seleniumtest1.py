from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\Pragati\Python_Selenium\Drivers_Browser\chromedriver_win32\chromedriver")
driver.get("https://appaccess.mphasis.com/")
driver.implicitly_wait(20)
print(driver.title)
print("URL of the page is "+driver.current_url)

driver.close()