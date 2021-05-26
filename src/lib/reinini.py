import configparser
import json
from pathlib import Path

def read_ini(path):
    """
        读取ini配置文件
    """
    config = configparser.ConfigParser()
    config.read(path, encoding='utf-8')
    return config

def to_list(config_key):
    p = str(Path(config_key))
    new_list = json.loads(p)
    return new_list

