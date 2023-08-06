#1
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.implicitly_wait(5)
#2
driver.execute_script("window.scrollBy(0, 600);")
#3
title_seleniumruby = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/selenium-ruby/'] h3").click()
#4
reviews_btn = driver.find_element_by_class_name("reviews_tab").click()
#5
stars = driver.find_element_by_class_name("star-5").click()
#6
text_field = driver.find_element_by_id("comment")
text_field.send_keys("Nice book!")
#7
name_field = driver.find_element_by_id("author")
name_field.send_keys("Raven")
#8
email_field = driver.find_element_by_id("email")
email_field.send_keys("soledad@bk.ru")
#9
submit_btn = driver.find_element_by_class_name("submit").click()