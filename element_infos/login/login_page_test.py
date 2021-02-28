import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utlis import logger
from common.base_page import BasePage
from common.browser import Browser

class LogionPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.kaiyuan_click = {'element_name': '点击开原版',
                                   'locator_type':'id',
                                   'locator_value':'zentao',
                                   'timeout': 3}
        self.user_name_inputbox = {'element_name':'用户名输入',
                                   'locator_type':'xpath',
                                   'locator_value':'//input[@name="account"]',
                                   'timeout': 5 }
        self.password_inputbox = {'element_name': '用户名密码',
                                   'locator_type': 'xpath',
                                   'locator_value': '//input[@name="password"]',
                                   'timeout': 4 }
        self.login_checkbox = {'element_name': '登录按钮',
                                   'locator_type': 'xpath',
                                   'locator_value': '//button[@id="submit"]',
                                   'timeout': 2 }
    # 方法--》控件的操作
    def clcik_kaiyuan(self):
        self.click(self.kaiyuan_click)

    def input_name(self,username):
        self.input(self.user_name_inputbox,username)


    # 方法--》控件的操作
    def input_password(self,password):
        self.input(self.password_inputbox, password)

    # 方法--》控件的操作
    def click_login(self):
        self.click(self.login_checkbox)

if __name__ == '__main__':
    # curren_path = os.path.dirname(__file__)
    # driver_path = os.path.join(curren_path, '../webdrver/chromedriver.exe')
    # driver = webdriver.Chrome(executable_path=driver_path)
    # driver = Browser().get_charmo_driver()
    driver = Browser().get_driver()

    login = LogionPage(driver)
    login.oper_url('http://127.0.0.1:81/index.php')
    login.clcik_kaiyuan()
    login.input_name('admin')
    login.input_password('Wyp123456')
    login.click_login()
    logger.info('运行了')