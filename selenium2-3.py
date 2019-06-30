from selenium import webdriver
import time

import math

from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x1 = browser.find_element_by_id('num1')
x = x1.text
y1 = browser.find_element_by_id('num2')
y = y1.text
z = int(x) + int(y)
print(z)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(z))


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

