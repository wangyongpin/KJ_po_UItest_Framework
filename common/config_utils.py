import configparser
import os

curren_dir = os.path.dirname(__file__)
config_path = os.path.join(curren_dir,"..","conf","config.ini")

class ConfingUtils:
    def __init__(self,path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path)

    @property
    def url(self):
        url_value = self.cfg.get('default','url')
        return url_value

    @property
    def driver_path(self):
        driver_path_value = self.cfg.get('default','driver_path')
        return driver_path_value

    @property
    def driver_name(self):
        driver_name_value = self.cfg.get('default', 'driver_name')
        return driver_name_value

    @property
    def time_out(self):
        time_out_value = float(self.cfg.get('default', 'time_out'))
        return time_out_value

    @property
    def screen_shot_path(self):
        screen_shot_path_value = self.cfg.get('default', 'screen_shot_path')
        return screen_shot_path_value

    @property
    def user_name(self):
        user_name_value = self.cfg.get('default', 'user_name')
        return user_name_value

    @property
    def password(self):
        password_value = self.cfg.get('default', 'password')
        return password_value

local_config = ConfingUtils()
if __name__ == '__main__':
    config = ConfingUtils()
    print(config.url)
    print(config.driver_path)
    print(config.driver_name)
    print(type(config.time_out))
    print(config.user_name)
    print(config.password)

