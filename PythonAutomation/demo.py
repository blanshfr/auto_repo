import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="C:\\WebDriver\\bin\\geckodriver.exe")

driver.maximize_window()


#driver.get("https://rahulshettyacademy.com/angularpractice/")


#print(driver.title)
#print(driver.current_url)

#driver.find_element_by_name("name").send_keys("Alex")
#driver.find_element_by_name("email").send_keys("alex@gmail.com")
#driver.find_element_by_id("exampleInputPassword1")
#dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")
#driver.find_element_by_class_name("btn").click()

#message = driver.find_element_by_class_name("alert-success").text

#if ("Unseccessfull" in message):
    #print("Test passed")
#else:
    #print("Test fails")
    #driver.close()

#------------------------------------------------------------------------------------------------------------
#driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#driver.find_element_by_id("autosuggest").send_keys("Ind")
#time.sleep(7)
#countries = driver.find_elements_by_css_selector("li[class = 'ui-menu-item'] a")
#for country in countries:
#    if country.text == "India":
#        country.click()
#        break
#assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"
#driver.close()

#-----------------------------------------------------------------------------------------------------------

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_css_selector("[id*='checkBoxOption']")
for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()


radio_buttons = driver.find_elements_by_name("radioButton")
for radio_button in radio_buttons:
    if radio_button.get_attribute("value") == "radio2":
        radio_button.click()
        assert radio_button.is_selected()

driver.find_element_by_name("enter-name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
assert "Option3" in alert.text

alert.accept()



driver.close()

