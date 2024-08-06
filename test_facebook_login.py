import pytest
from selenium.webdriver.common.by import By
from drivers import *
import time

class TestLogin:
    @pytest.mark.usefixtures("browser_chrome")
    def test_facebook_login_chrome(self, browser_chrome):
        self.driver = browser_chrome
        self.driver.get('https://www.facebook.com')

        email_input = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        email_input.send_keys('example@gmail.com')
        time.sleep(1)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        password_input.send_keys('abcdef')
        time.sleep(1)

        login_button = self.driver.find_element(By.NAME, 'login')
        login_button.click()
        time.sleep(10)

        self.driver.quit()

    @pytest.mark.usefixtures("browser_firefox")
    def test_facebook_login_firefox(self, browser_firefox):
        self.driver = browser_firefox
        self.driver.get('https://www.facebook.com')

        email_input = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        email_input.send_keys('example@gmail.com')
        time.sleep(1)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        password_input.send_keys('abcdef')
        time.sleep(1)

        login_button = self.driver.find_element(By.NAME, 'login')
        login_button.click()
        time.sleep(10)

        self.driver.quit()