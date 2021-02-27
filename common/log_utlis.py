import os,logging
current_paht = os.path.dirname(__file__)
log_path = os.path.join(current_paht,'../logs/test.log')

class LogUtils:
    def __init__(self,logfile_path = log_path):
        self.logfile_path = logfile_path
        self.logger = logging.getLogger('shizn实战日志') # 创建日志对象
        self.logger.setLevel(level=logging.INFO) # 设置日志级别
        # 创建一个文件类型的日志对象
        file_log = logging.FileHandler(self.logfile_path, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        file_log.setFormatter(formatter)# 使用日志格式
        self.logger.addHandler(file_log)  # 日志写入到文件中
    def info(self,message): #写正常的日志信息
        self.logger.info(message)

    def error(self,message): # 写错误日志信息
        self.logger.error(message)

logger = LogUtils()
# 测试
if __name__ == '__main__':
    log_test =  LogUtils()
    log_test.info('这是正常的日志信息')
    log_test.error('这是错误的日志信息')