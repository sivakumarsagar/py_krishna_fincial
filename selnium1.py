#from selenium import webdriver
#driver= webdriver.Chrome()
from selenium import webdriver
driver = webdriver.Chrome(executable_path= r'C:\Python38\geckodriver.exe')
browser = webdriver.Firefox()
#browser.get('http://inventwithpython.com')
driver.get("https://localhost:5000")

