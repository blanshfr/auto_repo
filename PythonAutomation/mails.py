from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="C:\\WebDriver\\bin\\geckodriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/")
driver.find_element_by_id("identifierId").send_keys("fortestingpurposes135@gmail.com")
driver.find_element_by_id("identifierId").send_keys(u'\ue007')
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.element_to_be_clickable((By.NAME, "password")))
driver.find_element_by_name("password").send_keys("R9dNFCGSbth99Gr")
driver.find_element_by_name("password").send_keys(u'\ue007')
driver.close()