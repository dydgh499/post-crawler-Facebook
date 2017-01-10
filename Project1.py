from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

f_id=open("id.txt","r");
f_pw=open("pw.txt","r");
id_line=f_id.readlines()
pw_line=f_pw.readlines()
line_count=0
for line in id_line:
    executable_path = "chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("https://www.facebook.com")
    print(driver.current_url)
    line=line.replace("\n","")
    pw_line[line_count]=pw_line[line_count].replace("\n", "")
    elem = driver.find_element_by_name('email')  # Find the search box
    elem.send_keys(line)
    elem = driver.find_element_by_name('pass')  # Find the search box
    elem.send_keys(pw_line[line_count])
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
    elem = driver.find_element_by_name('xhpc_message')
    t = time.gmtime()
    elem.send_keys(t.tm_sec)
    print(driver.current_url)
    act=driver.find_elements_by_xpath('//button[@type="submit"]')
    for i in act:
        g=str(i.get_attribute('class'))
        if(re.search('selected',g)):
            i.click()
            break

    time.sleep(3)
    driver.find_element_by_tag_name("body").click()
    logmu=driver.find_element_by_id('logoutMenu')
    logmu.click()
    time.sleep(5)
    logout = driver.find_element_by_xpath('//form[@action="https://www.facebook.com/logout.php"]')
    par = logout.find_element_by_xpath('..')
    par.click()
    time.sleep(3)
    driver.close()
    driver.quit()
