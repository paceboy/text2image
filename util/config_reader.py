
import configparser


class ConfigReader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def get_name_list(self):
        # 读取配置文件中名字列表
        if 'names' in self.config and 'name_list' in self.config['names']:
            return self.config['names']['name_list'].split(',')
        else:
            return []

    def get_ttf(self):
        # 读取配置文件中名字列表
        if 'ttf' in self.config and 'ttc' in self.config['ttf']:
            return self.config['ttf']['ttc']
        else:
            return []


# config_reader = ConfigReader('../conf/config.ini')
# name_list = config_reader.get_name_list()
# print("ConfigReader Name list:", name_list)