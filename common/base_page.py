from selenium import webdriver
import os,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.log_utlis import logger
from common.config_utils import local_config

class BasePage:
    def __init__(self,driver):
        self.driver =  webdriver.Chrome() #driver  driver

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

    def implicitly_wait(self,seconds=local_config.time_out):
        self.driver.implicitly_wait(seconds)

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
            # 显示等待封装

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

# selenium 执行js
    '''
    def __execute_script(self,js_string,element_info=None):
        if element_info:
            self.driver.execute_script(js_string)
        else:
            self.driver.execute_script(js_string,None)
    def  remover_element_attribute(self,element_info,attribute_name):
        # 移除属性
        element = self.find_element(element_info)
        self.__execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)
    def  update_element_attribute(self,element_info,attribute_name,attribute_value):
        # 修改属性
        element = self.find_element(element_info)
        self.__execute_script('arguments[0].setAttribute("%s","%s");'%(attribute_name,attribute_value),element)
    '''

    def  remover_element_attribute(self,element_info,attribute_name):
        # 移除属性
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)
    def  update_element_attribute(self,element_info,attribute_name,attribute_value):
        # 修改属性
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");'%(attribute_name,attribute_value),element)

    # frame ==> ID 和 NAME
    # 思路一
    def switch_to_frame(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
    # 思路二
    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)
    def switch_to_frame_by_element(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
    # 思路三
    def switch_to_frame1(self, **element_dict):
        self.wait()
        if  'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif  'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)


    # 等待
    def wait(self,seconds=local_config.time_out):
        time.sleep(seconds)

    # 等待默认值

