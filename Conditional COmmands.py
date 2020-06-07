from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="D:\Pragati\Python_Selenium\Drivers_Browser\chromedriver_win32\chromedriver")
driver.get("https://appaccess.mphasis.com/")
driver.maximize_window()
username=driver.find_element_by_name("username")
password=driver.find_element_by_name("password")
login=driver.find_element_by_id("submit")
time.sleep(5)
username.send_keys("2188615")
password.send_keys("+vethin2020")
login.click()
appaccess=driver.find_element_by_xpath("/html/body/div/a[1]/p")
appaccess.click()

driver.find_element_by_id("txtsearch").send_keys("office")
print("search")
driver.find_element_by_xpath("//*[@id='homesec']/img").click()
print("image")
driver.close()
time.sleep(10)
'''driver.find_element_by_xpath("//*[@id='i0116']").send_keys("pragati.h@mphasis.com")
driver.find_element_by_id("idSIButton9").click()
time.sleep(20)
driver.find_element_by_name("Password").send_keys("+vethin2020")
driver.find_element_by_xpath("//*[@id='submitButton']").click()
driver.find_element_by_xpath("//*[@id='ShellMail_link']/span").click()
#print("Appaccess is displayed")
time.sleep(10)
driver.close()'''
