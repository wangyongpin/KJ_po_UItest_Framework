from element_infos.login.login_page_test_excelone import LogionPage
# from element_infos.main.main_page_old import main_Project_Test
from element_infos.main.main_page import main_Project_Test
from common.config_utils import local_config

class QuitAction:
    def __init__(self,driver):
       self.main_page = main_Project_Test(driver)

    def quit(self):
        self.main_page.click_username()
        self.main_page.click_quit_button()
        return LogionPage(self.main_page.driver)