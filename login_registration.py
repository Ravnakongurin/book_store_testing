# # Регистрация аккаунта
# #1
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# my_account_tab = driver.find_element_by_link_text ("My Account").click()
# #3
# regmail_field = driver.find_element_by_id("reg_email")
# regmail_field.send_keys("soledad@bk.ru")
# #4
# regpassword_field = driver.find_element_by_id("reg_password")
# regpassword_field.send_keys("Ravnak0ngurin")
# #5
# register_btn = driver.find_element_by_css_selector("[name='register']").click()
#Логин в систему
#1
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.implicitly_wait(5)
#2
my_account_tab = driver.find_element_by_link_text ("My Account").click()
#3
email_field = driver.find_element_by_id("username")
email_field.send_keys("soledad@bk.ru")
#4
password_field = driver.find_element_by_id("password")
password_field.send_keys("Ravnak0ngurin")
#5
login_btn = driver.find_element_by_css_selector("[name='login']").click()
#6
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
logout = WebDriverWait(driver, 5).until(
EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))#проверка, что элемент есть и доступен для выбора