from locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
import test_data.data as td


class MainPage(BasePage):

    def click_newsletter_btn(self):
        WebDriverWait(self.driver, td.timeOut).until(EC.element_to_be_clickable(MainPageLocators.TONEWSLETTER_BUTTON))
        toNewsletter = self.driver.find_element(*MainPageLocators.TONEWSLETTER_BUTTON)
        toNewsletter.click()
