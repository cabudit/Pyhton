from selenium import webdriver
from selenium.webdriver.common.keys import Keys
Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.get(
    "https://www.topuniversities.com/university-rankings/world-university-rankings/2021")
driver.implicitly_wait(10)
rank = driver.find_element_by_css_selector(
    '#ranking-data-load ')
print(rank.text)
driver.close()
