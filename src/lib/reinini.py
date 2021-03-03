import configparser

def read_ini(path):
    """
        读取ini配置文件
    """
    config = configparser.ConfigParser()
    config.read(path, encoding='utf-8')
    return config

