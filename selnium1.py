#from selenium import webdriver
#driver= webdriver.Chrome()
from selenium import webdriver
driver = webdriver.Firefox(r'C:\Python38\geckodriver.exe')
#browser = webdriver.Firefox()
#browser.get('http://inventwithpython.com')
driver.get("https://localhost:5000")

