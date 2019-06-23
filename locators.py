from selenium import webdriver
from selenium.webdriver.common.by import By

TONEWSLETTER_CSS_SEL = 'div.z-navigation-footer_trackingWrap:nth-child(8) > a:nth-child(1)'
MENSFASHIONBUTTON_XPATH = "/html/body/div[4]/div[3]/div/div[2]/div/div[3]/div[1]/div/div[2]/label" #przepisac na uniwersalny xpath
EMAILFIELD_XPATH = '//*[starts-with(@id, "email")]'
SAVEBUTTON_XPATH = '/html/body/div[4]/div[3]/div/div[2]/div/form/button/span' #przepisac na uniwersalny xpath

class MainPageLocators:
    TONEWSLETTER_BUTTON = (By.CSS_SELECTOR, TONEWSLETTER_CSS_SEL)

class WhatFashionPageLocators:
    MENSFASHION_BUTTON = (By.XPATH, MENSFASHIONBUTTON_XPATH)

class SignUpPageLocators:
    EMAIL_FIELD = (By.XPATH, EMAILFIELD_XPATH)
    SAVE_BUTTON = (By.XPATH, SAVEBUTTON_XPATH)
