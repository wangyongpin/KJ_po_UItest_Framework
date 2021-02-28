import unittest
from actions.login_action import loginAction
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.oper_url(local_config.url)

    def tearDown(self) -> None:
        self.base_page.close_tab()

    def test_login_success(self):
        login_action = loginAction(self.base_page.driver)
        main_page = login_action.login_success('admin','Wyp123456')
        actual_result = main_page.get_username()
        # print(actual_result)
        self.assertEqual(actual_result,'admin','test_login_success登陆失败！')

if __name__ == '__main__':
    unittest.main()





