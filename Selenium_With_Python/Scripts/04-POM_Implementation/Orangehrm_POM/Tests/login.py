from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HtmlTestRunner

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from Orangehrm_POM.Pages.Loginpage import LoginPage
from Orangehrm_POM.Pages.homepage import Homepage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome("/home/lokesh/Orangehrm_POM/driver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login=LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        time.sleep(3)

        homepage=Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/lokesh/Orangehrm_POM/reports'))