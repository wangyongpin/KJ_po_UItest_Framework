import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from actions.login_action import loginAction
from common.log_utlis import logger
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.browser import Browser

driver = Browser().get_driver()
driver.get('http://127.0.0.1:81/index.php')
main_page = loginAction(driver).default_login()
value=main_page.get_username()
print(value)



