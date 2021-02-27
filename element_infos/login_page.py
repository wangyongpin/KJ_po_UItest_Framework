import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utlis import logger
curren_path = os.path.dirname(__file__)
driver_path = os.path.join(curren_path,'../webdrver/chromedriver.exe')
class LogionPage:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:81/index.php')
        #    属性--》页面的空间
        time.sleep(2)
        self.kaiyuan = self.driver.find_element(By.ID,'zentao').click()  # 点击开原版
        self.user_name_inputbox = self.driver.find_element(By.ID, 'account')
        self.password_inputbox = self.driver.find_element(By.NAME, 'password')
        self.login_checkbox= self.driver.find_element(By.ID, 'submit')

    # 方法--》控件的操作
    def input_name(self,username):
        self.user_name_inputbox.send_keys(username)

    # 方法--》控件的操作
    def input_password(self,password):
        self.password_inputbox.send_keys(password)

    # 方法--》控件的操作
    def click_login(self):
        self.login_checkbox.click()

if __name__ == '__main__':
    login = LogionPage()
    login.input_name('admin')
    login.input_password('Wyp123456')
    login.click_login()
    logger.info('运行了')