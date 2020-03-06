#from selenium import webdriver
#driver= webdriver.Chrome()
from selenium import webdriver
driver = webdriver.Chrome(r'C:\Python38\chromedriver.exe')
#browser = webdriver.Firefox()
#browser.get('http://inventwithpython.com')
driver.get("https://localhost:5000/")
driver.implicitly_wait(3000)
