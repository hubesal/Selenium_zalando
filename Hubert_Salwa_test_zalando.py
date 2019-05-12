from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

INVALID_EMAIL = "test"
TONEWSLETTER_CSS_SEL = 'div.z-navigation-footer_trackingWrap:nth-child(8) > a:nth-child(1)'
MENSFASSHIONBUTTON_XPATH = "/html/body/div[4]/div[3]/div/div[2]/div/div[3]/div[1]/div/div[2]/label"
EMAILFIELD_XPATH = '//*[starts-with(@id, "email")]'
SAVEBUTTON_XPATH = '/html/body/div[4]/div[3]/div/div[2]/div/form/button/span'
ERRORMSG_XPATH = '/html/body/div[4]/div[3]/div/div[2]/div/form/div/div/div/span[2]'

timeOut = 20

class TestZalando(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.delete_all_cookies()

    def test_newsletter(self):
        self.driver.get("https://www.zalando.pl/")
        WebDriverWait(self.driver, timeOut).until(EC.element_to_be_clickable((By.CSS_SELECTOR, TONEWSLETTER_CSS_SEL)))
        toNewsletter = self.driver.find_element_by_css_selector(TONEWSLETTER_CSS_SEL)
        toNewsletter.click()

        WebDriverWait(self.driver, timeOut).until(EC.element_to_be_clickable((By.XPATH, MENSFASSHIONBUTTON_XPATH)))
        mensFashionButton = self.driver.find_element_by_xpath(MENSFASSHIONBUTTON_XPATH)
        mensFashionButton.click()

        WebDriverWait(self.driver, timeOut).until(EC.presence_of_element_located((By.XPATH, EMAILFIELD_XPATH)))
        emailField = self.driver.find_element_by_xpath(EMAILFIELD_XPATH)
        emailField.send_keys(INVALID_EMAIL)

        WebDriverWait(self.driver, timeOut).until(EC.element_to_be_clickable((By.XPATH, SAVEBUTTON_XPATH)))
        saveButton = self.driver.find_element_by_xpath(SAVEBUTTON_XPATH)
        saveButton.click()

        self.driver.implicitly_wait(60)

        ErrorMessage = emailField.get_attribute('validationMessage')
        self.assertEqual(ErrorMessage, "Please enter an email address.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
