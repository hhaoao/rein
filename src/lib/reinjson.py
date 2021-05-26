import random
import json
import chardet
from jsonpath_ng import jsonpath, parse

class ReinJson:
    """
        读写 json
        
    """
    def __init__(self):
        self.info = ''
        self.jsonpath_expr = parse('architecture.*.url')

    def load(self, path):
        with open(path, 'r', encoding='utf-8-sig') as fo:
            data = json.loads(fo.read())
            self.info = data

    def store(self, data, path):
        with open(path, 'w', encoding='utf-8-sig') as fw:
            json.dump(data, fw)

    def get_url(self, version_package):
        # 是否简单模式 or 版本存在 
        if "url" in self.info:
            url = self.info["url"]
        else:
            if "url" in self.info["architecture"]:
                url = self.info["architecture"]["url"]
            elif version_package in self.info["architecture"]:
                url = self.info["architecture"][version_package]["url"]
            else:
                url = [match.value for match in self.jsonpath_expr.find(self.info)]
        
        # 单个安装包多链接处理
        if isinstance(url, list):
            # 无预处理则取第一个连接 有预处理(辅助文件)则全部下载
            if not "pre_install" in self.info:
                random_url = random.choice(url)
                url = [ random_url ]
        else:
            url = [ url ]

        return url
