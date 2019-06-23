from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_data.data as td
from base_page import BasePage
from locators import WhatFashionPageLocators

class WhatFashionPage(BasePage):

    def click_mens_fashion_btn(self):
        WebDriverWait(self.driver, td.timeOut).until(EC.element_to_be_clickable(WhatFashionPageLocators.MENSFASHION_BUTTON))
        mensFashionButton = self.driver.find_element(*WhatFashionPageLocators.MENSFASHION_BUTTON)
        mensFashionButton.click()
