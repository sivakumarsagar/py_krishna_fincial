#from selenium import webdriver
#driver= webdriver.Chrome()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Python38\chromedriver.exe')
#browser = webdriver.Firefox()
#browser.get('http://inventwithpython.com')
driver.get("http://localhost:5000/application.html")
name=driver.find_element_by_name("name")
email=driver.find_element_by_name("email")
age=driver.find_element_by_name("age")
gender=driver.find_element_by_name("gender")
married=driver.find_element_by_name("married")
dependents=driver.find_element_by_name("dependents")
education=driver.find_element_by_name("education")
appincome=driver.find_element_by_name("appincome")
coappincome=driver.find_element_by_name("coappincome")
loan_amount=driver.find_element_by_name("loan_amount")
loan_term=driver.find_element_by_name("loan_term")
credit_history=driver.find_element_by_name("credit_history")
area=driver.find_element_by_name("area")
employment=driver.find_element_by_name("employment")

name.get_attribute('value')
email.get_attribute('value')
age.get_attribute('value')
gender.get_attribute('value')
married.get_attribute('value')
dependents.get_attribute('value')
education.get_attribute('value')
appincome.get_attribute('value')
coappincome.get_attribute('value')
loan_amount.get_attribute('value')
loan_term.get_attribute('value')
credit_history.get_attribute('value')
area.get_attribute('value')
employment.get_attribute('value')


driver.implicitly_wait(300000)
