from element_infos.login.login_page_test_excelone import LogionPage
# from element_infos.main.main_page_old import main_Project_Test
from element_infos.main.main_page import main_Project_Test
from common.config_utils import local_config

class loginAction:
    def __init__(self,driver):
       self.login_page = LogionPage(driver)
       # self.main_page = main_Project_Test(driver)
    def login_action(self,username,password):
        self.login_page.clcik_kaiyuan()  # 开原版
        self.login_page.input_name(username)
        self.login_page.input_password(password)
        self.login_page.click_login() # 登录

    def login_success(self,username,password):
        self.login_action(username,password)
        return main_Project_Test( self.login_page.driver)

    def default_login(self):
       return self.login_success(local_config.user_name,local_config.password)

    def login_fail(self,username,password):
        self.login_action(username, password)
        return  self.login_page.get_login_fail_alert_content()

    def login_by_coolie(self):
        pass



