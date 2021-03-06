from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/tmp/ChromeProfile")

driver = webdriver.Chrome(options=options)
driver.get("https://tinder.com/")

MAX_AGE = 19
MIN_AGE = 18

while "1" != input("press 1 when signed in: "):
    pass
while True:
    age = driver.find_elements_by_xpath('.//span[@itemprop="age"]')
    age = age[1].text
    print("Age = ", age)
    if int(age) <= MAX_AGE and int(age) >= MIN_AGE:
        driver.find_element_by_css_selector('body').send_keys(Keys.ARROW_RIGHT)
    else:
        driver.find_element_by_css_selector('body').send_keys(Keys.ARROW_LEFT)
    
    sleep(2)