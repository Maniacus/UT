from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

#ждем когда искомы элемент примет нужное значение
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
)
print(1)

button1 = browser.find_element_by_id("book")
#browser.execute_script("window.scrollBy(0, 100);")
button1.click()
print(2)

x1 = browser.find_element_by_id('input_value')
x = int(x1.text)
z = calc(x)

ans = browser.find_element_by_css_selector('input[id="answer"]')
ans.send_keys(z)

button2 = browser.find_element_by_id("solve")
#browser.execute_script("window.scrollBy(0, 100);")
button2.click()


assert "успешно" in message.text