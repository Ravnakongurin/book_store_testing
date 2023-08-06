# # Отображение страницы товара
# #1
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# my_account_tab = driver.find_element_by_link_text ("My Account").click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("soledad@bk.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("Ravnak0ngurin")
# login_btn = driver.find_element_by_css_selector("[name='login']").click()
# #3
# shop_tab = driver.find_element_by_id("menu-item-40").click()
# #4
# html5forms = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/html5-forms/']").click()
# #5
# cover = driver.find_element_by_css_selector(".woocommerce-main-image > img")
# book_title = cover.get_attribute("title")
# print ("Название: ", book_title) #для наглядности
# assert book_title == "HTML5 Forms"
# Количество товаров в категории
# #1
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# my_account_tab = driver.find_element_by_link_text ("My Account").click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("soledad@bk.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("Ravnak0ngurin")
# login_btn = driver.find_element_by_css_selector("[name='login']").click()
# #3
# shop_tab = driver.find_element_by_id("menu-item-40").click()
# #4
# html_tab = driver.find_element_by_css_selector(".cat-item-19 > a").click()
#5
# проверка по счетчику
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# count_html= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cat-item-19 > span"), "(3)"))
# или непосредственно
# items = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# items_count = len(items)
# assert items_count == 3
# Сортировка товаров
# #1
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# my_account_tab = driver.find_element_by_link_text ("My Account").click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("soledad@bk.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("Ravnak0ngurin")
# login_btn = driver.find_element_by_css_selector("[name='login']").click()
# #3
# shop_tab = driver.find_element_by_id("menu-item-40").click()
# #4
# selector = driver.find_element_by_class_name("orderby")
# selector_value = selector.get_attribute("value")
# assert selector_value == "menu_order"
# #5
# from selenium.webdriver.support.select import Select
# selector = driver.find_element_by_class_name("orderby")
# select = Select(selector)
# select.select_by_value("price-desc")
# #6
# selector = driver.find_element_by_class_name("orderby")
# #7
# selector_value = selector.get_attribute("value")
# assert selector_value == "price-desc"
#Отображение, скидка товара
# #1
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# my_account_tab = driver.find_element_by_link_text ("My Account").click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("soledad@bk.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("Ravnak0ngurin")
# login_btn = driver.find_element_by_css_selector("[name='login']").click()
# #3
# shop_tab = driver.find_element_by_id("menu-item-40").click()
# #4
# android_book = driver.find_element_by_css_selector("[title='Android Quick Start Guide']").click()
# #5
# old_price = driver.find_element_by_css_selector("del > span")
# old_price_value = old_price.text
# assert old_price_value == "₹600.00"
# #6
# new_price = driver.find_element_by_css_selector("ins > span")
# new_price_value = new_price.text
# assert new_price_value == "₹450.00"
# #7
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# wait = WebDriverWait(driver, 5)
# cover = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "zoom")))
# cover.click()
# #8
# close_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# close_btn.click()
# # Проверка цены в корзине
# #1
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# shop_tab = driver.find_element_by_id("menu-item-40").click()
# #3
# add_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# #4
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# wait = WebDriverWait(driver, 5)
# cart_quantity = wait.until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "cartcontents"), "1 Item"))
# cart_price = driver.find_element_by_css_selector(".wpmenucart-contents > .amount")
# cart_price_value = cart_price.text
# assert cart_price_value == "₹180.00"
# #5
# cart = driver.find_element_by_id("wpmenucartli").click()
# #6
# subtotal = wait.until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .amount"), "₹180.00"))
# #7
# total = wait.until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .amount"), "₹183.60"))
# Работа в корзине
# #1
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# shop_tab = driver.find_element_by_id("menu-item-40").click()
# #3
# driver.execute_script("window.scrollBy(0, 300);")
# add_book1_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# time.sleep(3)
# add_book2_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']").click()
# #4
# cart = driver.find_element_by_id("wpmenucartli").click()
# #5
# time.sleep(3)
# remove1 = driver.find_element_by_css_selector(".remove[data-product_id='182']").click()
# #6
# undo = driver.find_element_by_css_selector(".woocommerce-message > a").click()
# #7
# time.sleep(3)
# quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1) .quantity > input")
# quantity.clear()
# quantity.send_keys("3")
# #8
# update_btn = driver.find_element_by_css_selector(".button[name='update_cart']").click()
# #9
# quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1) .quantity > input")
# quantity_check = quantity.get_attribute("value")
# assert quantity_check == "3"
# #10
# time.sleep(3)
# apply_btn = driver.find_element_by_css_selector(".button[name='apply_coupon']").click()
# #11
# response = driver.find_element_by_class_name("entry-content")
# response_text = response.text
# assert "Please enter a coupon code." in response_text
#Покупка товара
#1
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.implicitly_wait(5)
#2
shop_tab = driver.find_element_by_id("menu-item-40").click()
#3
driver.execute_script("window.scrollBy(0, 300);")
add_book1_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
time.sleep(3)
add_book2_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']").click()
#4
cart = driver.find_element_by_id("wpmenucartli").click()
#5
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 5)
checkout_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn.click()
#6
form = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-billing-fields")))
first_name_field = driver.find_element_by_id("billing_first_name")
first_name_field.send_keys("Jane")
last_name_field = driver.find_element_by_id("billing_last_name")
last_name_field.send_keys("Doe")
email_field = driver.find_element_by_id("billing_email")
email_field.send_keys("soledad@bk.ru")
phone_field = driver.find_element_by_id("billing_phone")
phone_field.send_keys("+79152773377")
country_select = driver.find_element_by_id("s2id_billing_country").click()
country_field = driver.find_element_by_id("s2id_autogen1_search")
country_field.send_keys("Russia")
country = driver.find_element_by_class_name("select2-result-label").click()
address_field = driver.find_element_by_id("billing_address_1")
address_field.send_keys("Red Square,1")
city_field = driver.find_element_by_id("billing_city")
city_field.send_keys("Moscow")
state_field = driver.find_element_by_id("billing_state")
state_field.send_keys("Moscow")
zip_field = driver.find_element_by_id("billing_postcode")
zip_field.send_keys("125000")
#7
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payment = driver.find_element_by_id("payment_method_cheque").click()
#8
place_order_btn = driver.find_element_by_id("place_order").click()
#9
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)
text1_check = wait.until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "entry-content"), "Thank you. Your order has been received."))
#10
text2_check = wait.until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))