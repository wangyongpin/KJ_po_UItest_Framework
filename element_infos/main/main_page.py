import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By

from common.log_utlis import logger
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.browser import Browser
# from actions.login_action import loginAction

class main_Project_Test(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements = ElementdataUtils('main','main_page').get_element_info()
        self.myzone_link = elements['myzone_link']
        self.user_menu = elements['user_menu']

    def  goto_myzone(self): # 进入我的地盘菜单
        self.click(self.myzone_link)

    def get_username(self):
        value = self.get_text(self.user_menu)
        return value
if __name__ == '__main__':
    driver = Browser().get_driver()
    # driver.get('http://127.0.0.1:81/index.php')
    # # main_page = loginAction(driver).default_login()
    # value=main_page.get_username()
    # print(value)



