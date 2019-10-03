from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("../driver/chromedriver")

driver.set_page_load_timeout("5")
driver.get("http://google.com")
driver.maximize_window()

element=driver.find_element_by_name("q")
element.send_keys("Lokesh Sharma")
element.submit()


driver.refresh()

time.sleep(4)
driver.quit()