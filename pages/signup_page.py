from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_data.data as td
from base_page import BasePage
from locators import SignUpPageLocators

class SignUpPage(BasePage):

    def getEmailField(self):
        return self.driver.find_element(*SignUpPageLocators.EMAIL_FIELD)

    def fulfill_email_field(self, emailData):
        WebDriverWait(self.driver, td.timeOut).until(EC.presence_of_element_located(SignUpPageLocators.EMAIL_FIELD))
        self.getEmailField().send_keys(emailData)

    def click_save_button(self):
        WebDriverWait(self.driver, td.timeOut).until(EC.element_to_be_clickable(SignUpPageLocators.SAVE_BUTTON))
        saveButton = self.driver.find_element(*SignUpPageLocators.SAVE_BUTTON)
        saveButton.click()

    def check_error_message(self):
        ErrorMessage = self.getEmailField().get_attribute('validationMessage')
        return ErrorMessage
