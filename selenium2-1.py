from selenium import webdriver
import time

import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element_by_css_selector('span[id="input_value"]')
x = x_element.text
y = calc(x)

print(y)

ans = browser.find_element_by_css_selector('input[id="answer"]')
ans.send_keys(y)

element1 = browser.find_element_by_css_selector('input[id="robotCheckbox"]')
element1.click()

element2 = browser.find_element_by_css_selector('input[id="robotsRule"]')
element2.click()



# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text