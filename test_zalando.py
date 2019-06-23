from selenium import webdriver
from pages.main_page import MainPage
from pages.fashion_page import WhatFashionPage
from pages.signup_page import SignUpPage
import unittest
import test_data.data as td

class TestZalando(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.delete_all_cookies()
        self.driver.get(td.mainpage)

    def test_newsletter(self):
        mainpage = MainPage(self.driver)
        mainpage.click_newsletter_btn()

        whatfashionpage = WhatFashionPage(self.driver)
        whatfashionpage.click_mens_fashion_btn()

        signuppage = SignUpPage(self.driver)
        signuppage.fulfill_email_field(td.INVALID_EMAIL)
        signuppage.click_save_button()
        signuppage.check_error_message()

        self.assertEqual(signuppage.check_error_message(), "Please enter an email address.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
