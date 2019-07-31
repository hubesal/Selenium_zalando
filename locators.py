from selenium import webdriver
from selenium.webdriver.common.by import By

TONEWSLETTER_CSS_SEL = 'div.z-navigation-footer_trackingWrap:nth-child(8) > a:nth-child(1)'
MENSFASHIONBUTTON_XPATH = '//label[@for="2"]'
EMAILFIELD_XPATH = '//input[starts-with(@id, "email")]'
SAVEBUTTON_XPATH = '//button[contains(@class, "form__btn")]'



class MainPageLocators:
    TONEWSLETTER_BUTTON = (By.CSS_SELECTOR, TONEWSLETTER_CSS_SEL)

class WhatFashionPageLocators:
    MENSFASHION_BUTTON = (By.XPATH, MENSFASHIONBUTTON_XPATH)

class SignUpPageLocators:
    EMAIL_FIELD = (By.XPATH, EMAILFIELD_XPATH)
    SAVE_BUTTON = (By.XPATH, SAVEBUTTON_XPATH)
