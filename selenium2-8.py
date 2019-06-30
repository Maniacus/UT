from selenium import webdriver
import math

import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)




button = browser.find_element_by_tag_name("button")
#browser.execute_script("window.scrollBy(0, 100);")
button.click()

print(1)


#alert = browser.switch_to.alert
#alert.accept()

print(2)

print(browser.window_handles)
#определеям окно
new_window = browser.window_handles[1]
#переключаемся на него
browser.switch_to.window(new_window)


x1 = browser.find_element_by_id('input_value')
x = int(x1.text)
z = calc(x)

ans = browser.find_element_by_css_selector('input[id="answer"]')
ans.send_keys(z)

button = browser.find_element_by_tag_name("button")
#browser.execute_script("window.scrollBy(0, 100);")
button.click()



#element1 = browser.find_element_by_css_selector('input[placeholder="Введите имя"]').send_keys('Андрей')
#element2 = browser.find_element_by_css_selector('input[placeholder="Введите фамилию"]').send_keys('Бердник')
#element3 = browser.find_element_by_css_selector('input[placeholder="Введите Email"]').send_keys('berdnik@gmail.com')

#current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
#file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

#element4 = browser.find_element_by_name('file')
#element4.send_keys(file_path)



