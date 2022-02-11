from selenium import webdriver
import time
from math import log, sin 
import os

def calc(x):
  return str(log(abs(12*sin(x))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)

    z = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(z)

    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()