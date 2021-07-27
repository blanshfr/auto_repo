import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="C:\\WebDriver\\bin\\geckodriver.exe")
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_xpath("//div[@class = 'example']/a").click()

driver.switch_to.window(driver.window_handles[1])
print(driver.find_element_by_xpath("//h3").text)

driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_xpath("//h3").text)



driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").send_keys("I am here")
