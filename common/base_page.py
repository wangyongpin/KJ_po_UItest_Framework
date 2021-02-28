from lib2to3.pgen2 import driver
from telnetlib import EC

from selenium import webdriver
import os,time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from common.log_utlis import logger
from common.config_utils import local_config

class BasePage:
    def __init__(self,driver):
        self.driver =  webdriver.Chrome() #driver  driver
        # self.chains = ActionChains(self.driver) # 鼠标默认，下面封装会使用---不推荐受使用，鼠标操作太少

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

    # 鼠标键盘封装（建议代码思路，判断操作系统）
    def move_to_element_by_mouse(self,element_info): # 移动到指定位置
        element = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    def long_press_element(self,element_info,senconds): # 长按并且释放
        element = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(senconds).release(element)





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
# 弹窗狂封装
    def switch_to_alert(self,action='accept',time_out=local_config.time_out):
        self.wait(time_out)
        alter = self.driver.switch_to.alert()
        alter_text = alter.text
        if action == 'accept':
            alter.accept()
        elif action == 'dismiss':
            alter.dismiss()
        return alter_text

# windows句柄封装

    def get_windw_handls(self):
        return self.driver.current_window_handle
    def switck_to_window_byhandle(self,window_handle):
        self.driver.switch_to.window(window_handle)
    def switck_to_window_by_title(self,title): # 根据title判断
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(driver,local_config.time_out).until(EC.title_contais(title)):
                self.driver.switch_to.window(window_handle)
                break
    def switck_to_window_by_url(self,url): # 根据url判断
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(driver,local_config.time_out).until(EC.url_contais(url)):
                self.driver.switch_to.window(window_handle)
                break

# 截图

    def screensshot_as_file(self,*screenshot_path):
        if len(screenshot_path) == 0:
            screenshot_filepath = local_config.screen_shot_path
        else:
            screenshot_filepath = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        current_dir = os.path.abspath(os.path.dirname(__file__))
        screenshot_filepath = os.path.join(current_dir,screenshot_filepath,'UITest.%s.png' %now)
        self.__driver.get_screenshot_as_file(screenshot_filepath)

    # 等待
    def wait(self,seconds=local_config.time_out):
        time.sleep(seconds)

    # 等待默认值

