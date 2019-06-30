from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)
#Поиск инпута для имени
element1 = browser.find_element_by_css_selector('input[placeholder="Введите имя"]')
print(element1)
element1.send_keys("Мой ответ")

#Поиск инпута для фамилии
element2 = browser.find_element_by_css_selector('input[placeholder="Введите фамилию"]')
print(element2)
element2.send_keys("Мой ответ")

#Поиск инпута для элпочты
element3 = browser.find_element_by_css_selector('input[placeholder="Введите Email"]')
print(element3)
element3.send_keys("Мой ответ")

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