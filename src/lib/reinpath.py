from pathlib import Path
import re

def search_just(directory='buckets', files_glob='**/*.json'):
    """
        批量搜索文件
    """
    p = Path(directory)
    files_list = (i for i in p.glob(files_glob))
    return files_list

def search_packages(package_name_list, directory='buckets', files_glob='**/*.json'):
    """
        搜索指定包
    """
    packages_target, packages__not_target = [], []
    packages_all = search_just(directory, files_glob)
    # packages_all = list(packages_all)
    for i in package_name_list:
        for j in packages_all:
            if j.stem == i:
                packages_target.append(j)
                break
        else:
            packages__not_target.append(i)

    if not packages_target:
        packages_target, packages__not_target = ['***'], package_name_list
    return packages_target, packages__not_target

def find_bucket_path(path):
    """
        return buckets path list

    """
    buckets_path, m = [], None
    buckets = search_just(directory=path, files_glob='*/')
    pattern = re.compile(".*\$psscriptroot/(.*)\"")
    for i in buckets:
        p = i / 'bin'
        p = search_just(p, '*.ps1')
        for k in p:
            with open(str(k), 'r', encoding='utf-8') as f:
                for j in f:
                    m = pattern.match(j)
                    if m:
                        break
            if m:
                bucket_path = k.parent.joinpath(m.group(1)).resolve()
                buckets_path.append(str(bucket_path))
                break
    return buckets_path
    
