from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


x1 = browser.find_element_by_id('input_value')
x = int(x1.text)
z = calc(x)

ans = browser.find_element_by_css_selector('input[id="answer"]')
ans.send_keys(z)

button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 100);")

element1 = browser.find_element_by_css_selector('input[id="robotCheckbox"]')
element1.click()

element2 = browser.find_element_by_css_selector('input[id="robotsRule"]')
element2.click()


button.click()
