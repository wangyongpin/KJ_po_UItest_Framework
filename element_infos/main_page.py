from selenium import webdriver
import os,time
from selenium.webdriver.common.by import By
from element_infos.login_page import LogionPage # 导入登录包
from common.log_utlis import logger

class main_Project_Test:
    def __init__(self):
        login = LogionPage()
        login.input_name('admin')
        login.input_password('Wyp123456')
        login.click_login()
        self.driver = login.driver # 把login_page的对象移动到main_Project_Test
        self.companyname_showbox = self.driver.find_element(By.ID,'companyname') # 点击易软天创
        self.myzone_menu = self.driver.find_element(By.XPATH,'//li[@class="active"]') # 我的地盘
        self.product_menu = self.driver.find_element(By.XPATH,'//li[@data-id="product"]') # 产品
        self.username_shhowspan = self.driver.find_element(By.XPATH, '//span[@class="user-name"]')  # 点击登录人

    def companyname_showbox(self): # 获取公司名称
        value1 = self.companyname_showbox.get_attribute('title')
        logger.info('这是获取公司名称')
        return value1

    def myzone_menu(self): # 进入我的地盘菜单
        self.myzone_menu.click()

    def product_menu(self): # 进入我的产品菜单
        self.product_menu.click()
        logger.info('这是点击产品菜单')

    def get_username(self): # 点击我的用户
        value = self.username_shhowspan.text
        logger.info('这是获取用户名成功：用户名是'+str(value))
        return value

if __name__ == '__main__':
    main_page = main_Project_Test()
    username = main_page.get_username()
    print(username)
    logger.info('运行结束')

