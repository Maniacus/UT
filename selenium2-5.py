from selenium import webdriver
import math

import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


element1 = browser.find_element_by_css_selector('input[placeholder="Введите имя"]').send_keys('Андрей')
element2 = browser.find_element_by_css_selector('input[placeholder="Введите фамилию"]').send_keys('Бердник')
element3 = browser.find_element_by_css_selector('input[placeholder="Введите Email"]').send_keys('berdnik@gmail.com')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

element4 = browser.find_element_by_name('file')
element4.send_keys(file_path)



button = browser.find_element_by_tag_name("button")
#browser.execute_script("window.scrollBy(0, 100);")
button.click()
