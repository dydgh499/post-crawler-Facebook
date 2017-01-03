from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

f_id=open("id.txt","r");
f_pw=open("pw.txt","r");

executable_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get("http://www.facebook.com")

id=f_id.readline()
print(id)
pw=f_pw.readline()
print(pw)
elem = driver.find_element_by_name('email')  # Find the search box
elem.send_keys(id)
elem = driver.find_element_by_name('pass')  # Find the search box
elem.send_keys(pw)
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_name('xhpc_message')
elem.send_keys("test")
elem.send_keys(Keys.RETURN)

time.sleep(15)

driver.close()
driver.quit()