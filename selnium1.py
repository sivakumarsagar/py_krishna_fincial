import sqlite3

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Python38\chromedriver.exe')
#browser = webdriver.Firefox()
driver.get("http://localhost:5000/application.html")
name=driver.find_element_by_name("name")
email=driver.find_element_by_name("email")
age=driver.find_element_by_name("age")
appincome=driver.find_element_by_name("appincome")
coappincome=driver.find_element_by_name("coappincome")
loan_amount=driver.find_element_by_name("loan_amount")
loan_term=driver.find_element_by_name("loan_term")
name.send_keys('Siva Kumar')
email.send_keys('aa@gmail.com')
age.send_keys('33')
appincome.send_keys('0')
coappincome.send_keys('0')
loan_amount.get_attribute('0')
loan_term.send_keys('0')
driver.find_element_by_css_selector("input[type='radio'][name='gender'][value='1']").click()
driver.find_element_by_css_selector("input[type='radio'][name='married'][value='0']").click()
driver.find_element_by_css_selector("input[type='radio'][name='dependents'][value='2']").click()
driver.find_element_by_css_selector("input[type='radio'][name='education'][value='1']").click()
driver.find_element_by_css_selector("input[type='radio'][name='employment'][value='1']").click()
driver.find_element_by_css_selector("input[type='radio'][name='credit_history'][value='0']").click()
driver.find_element_by_css_selector("input[type='radio'][name='area'][value='2']").click()
driver.find_element_by_xpath("//form//input[@type='submit' and @value='Submit']").click()
driver.close()
