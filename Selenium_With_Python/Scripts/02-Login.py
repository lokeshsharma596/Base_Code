from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("../driver/chromedriver")

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

#Login
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

time.sleep(3)

#Logout
driver.find_element_by_id("welcome").click()
driver.find_element_by_link_text("Logout").click()



driver.close()
driver.quit()

print("Test Completed")
