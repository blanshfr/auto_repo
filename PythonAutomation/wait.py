import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="C:\\WebDriver\\bin\\geckodriver.exe")

driver.maximize_window()

list = []
list2 = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
#driver.implicitly_wait(5)
driver.find_element_by_class_name("search-keyword").send_keys("ber")
time.sleep(4)
to_carts = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")
for button in to_carts:
    button.click()
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)

print(list)
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "cart-icon")))
driver.find_element_by_xpath("//a[@class = 'cart-icon']/img").click()
driver.find_element_by_xpath("//div[@class = 'action-block']/button").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
promo_info = driver.find_element_by_class_name("promoInfo").text
assert promo_info == "Code applied ..!"


vegs = driver.find_elements_by_css_selector("p.product-name")
for veg in vegs:
    list2.append(veg.text)
print(list2)
assert list == list2

totalAmount = int(driver.find_element_by_class_name("totAmt").text)
discountAmount = float(driver.find_element_by_class_name("discountAmt").text)
assert totalAmount > discountAmount

sum = 0
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
for amount in amounts:
    amount = int(amount.text)
    sum = sum + amount
print(sum)
assert sum == totalAmount


driver.close()