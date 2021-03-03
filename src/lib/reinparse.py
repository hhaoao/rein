import argparse

def rein_arg_parse():
    parser = argparse.ArgumentParser(description='下载安装包的小工具')
    parser.add_argument('--download',
            metavar='package',
            nargs='+',
            help='下载安装包, 包名,分隔符为空格')
    parser.add_argument('--updata',
            action='store_true',
            help='强制更新buckets')
    parser.add_argument('--search',
            metavar='package',
            nargs='+',
            help='搜索安装包, 包名,分隔符为空格')
    args = parser.parse_args()
    return args
