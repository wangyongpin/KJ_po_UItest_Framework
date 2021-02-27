from selenium import webdriver
import os,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.log_utlis import logger

class BasePage:
    def __init__(self,driver):
        self.driver = driver # driver

    # 浏览器操作的封装--->二次封装
    def oper_url(self,url):
        self.driver.get( url )
        logger.info('打开URL地址 % s' % url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')

    def refrseh(self):
        self.driver.refresh()
        logger.info('刷新')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页的title %s' %value)
        return value

    #........

    # 元素操作封装
    # element_info
    def  find_element(self,element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name =='id':
            locator_type = By.ID
        elif locator_type_name == 'name':
            locator_type = By.NAME
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        element = WebDriverWait(self.driver,locator_timeout) \
            .until(lambda x:x.find_element(locator_type,locator_value_info))
        logger.info('[%s]元素识别成功' %element_info['element_name'])
        return element

    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素进行了点击'%element_info['element_name'])

    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容%s' % (element_info['element_name'],content))
