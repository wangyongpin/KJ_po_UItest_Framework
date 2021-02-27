import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utlis import logger
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils

class LogionPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements = ElementdataUtils('login_page').get_element_info()
        self.kaiyuan_click = elements['kaiyuan_click']
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']
        # 方法--》控件的操作
    def clcik_kaiyuan(self):
        self.click(self.kaiyuan_click)

    def input_name(self, username):
        self.input(self.username_inputbox, username)

        # 方法--》控件的操作
    def input_password(self, password):
        self.input(self.password_inputbox, password)

        # 方法--》控件的操作
    def click_login(self):
        self.click(self.login_button)

if __name__ == '__main__':
    curren_path = os.path.dirname(__file__)
    driver_path = os.path.join(curren_path, '../webdrver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    login = LogionPage(driver)
    login.oper_url('http://127.0.0.1:81/index.php')
    login.clcik_kaiyuan()
    login.input_name('admin')
    login.input_password('Wyp123456')
    login.click_login()
    print('运行成功')
    logger.info('运行了')