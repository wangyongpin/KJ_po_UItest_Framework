import os,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.config_utils import local_config

curren_path = os.path.abspath(os.path.dirname(__file__))
dri_path = os.path.join(curren_path, '..', local_config.driver_path)

print(dri_path)
class Browser:
    def __init__(self,driver_path = dri_path,driver_name = local_config.driver_name):
        self.__driver_path = driver_path
        self.__driver_name = driver_name

    def get_driver(self):
        # 使用默认的配置
        if self.__driver_name.lower() == "chrome" :
            return self.__get_charmo_driver()
        elif self.__driver_name.lower() == "firefox" :
            return self.__get_firefox_driver()
        elif self.__driver_name.lower() == "edge" :
            return self.__get_edge_driver()

    def __get_charmo_driver(self):
        chrome_optinos = Options()
        chrome_optinos.add_argument('--disable-gpu') # 谷歌文档里面提到需要这个属性来规避BUG
        chrome_optinos.add_argument('lang=zh_CN.UTF-8') # 设置默认编码为utf-8
        chrome_optinos.add_experimental_option('useAutomationExtension',False) # 取消谷歌受到的自动控制提醒
        chrome_optinos.add_experimental_option('excludeSwitches',['enable-automation'])# 取消谷歌受到的自动控制提醒
        chrome_driver_path = os.path.join(self.__driver_path,'chromedriver.exe')
        driver = webdriver.Chrome(options=chrome_optinos,executable_path=chrome_driver_path)
        return driver

    def __get_firefox_driver(self):
        firefox_driver_path = os.path.join(self.__driver_path,'geckodriver.exe')
        driver = webdriver.Chrome(executable_path=firefox_driver_path)
        return driver

    def __get_edge_driver(self):
        ie_driver_path = os.path.join(self.__driver_path,'MicrosoftwebDriver.exe')
        print(ie_driver_path)
        driver = webdriver.Chrome(executable_path=ie_driver_path)
        return driver

    def __get_remote_driver(self):  # selenium 支持分布式 配置~~自己研究
        pass
if __name__ == '__main__':
    Browser().get_charmo_driver()

