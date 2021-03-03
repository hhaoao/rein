from pathlib import Path
import sys
import re

from lib import (
    reindownload,
    reinjson,
    reinparse,
    reinpath,
    reinini,
    reindatabases,
    reingit,
)

def buckets_storage(bucket_path):
    packages_all = reinpath.search_just(directory=bucket_path)
    single_package_list = [ (i.stem, str(i)) for i in packages_all ]
    datase.packages_storage(single_package_list)
    return 1

def download(package_path):
    package_json.load(package_path)
    urls = package_json.get_url(architecture)
    urls = [i for i in urls if not pattern.match(i)]
    print(urls)
    # reindownload.ReinDownload.add_urls(urls)

def get_info(package):
    package_path = package[1]
    package_path_parts = Path(package_path).parts
    package_bucket_parts = Path(buckets_path_file).parts
    difference = list(set(package_path_parts).difference(set(package_bucket_parts)))
    difference.sort(key=package_path_parts.index)
    p = difference[0] + "/" + package[0] + " "
    package_json.load(package_path)
    version = package_json.info["version"]
    if "description" in package_json.info:
        description = package_json.info["description"]
    else:
        description = package_json.info["homepage"]
    return p, version, description


if __name__ == "__main__":
    args = reinparse.rein_arg_parse()

    package_json = reinjson.ReinJson()

    package_download = reindownload.ReinDownload()
    pattern = re.compile(".*\.(reg|ico)$")

    rein_ini_path = Path(sys.argv[0]).parent / 'rein.ini'
    config = reinini.read_ini(str(rein_ini_path))
    architecture = config['rein']['architecture'] + "bit"
    buckets_path_file = config['rein']['buckets']
    
    buckets_path = reinpath.find_bucket_path(buckets_path_file)
    git_root_path = reinpath.search_just(files_glob='*/.git')
    
    datase = reindatabases.sqlite()
    datase.create_table()

    if args.updata:
        for x in git_root_path:
            pull_info = reingit.update_force(str(x.parent))
            print(pull_info)

    # 入库
    state = [ buckets_storage(i) for i in buckets_path ]

    if args.download:
        target_packages = [ x for j in args.download for x in datase.query(j) ]
        aa = datase.conn.execute('SELECT * FROM manager')

        # for i in target_packages:
        for i in aa:
            download(i[1])

    if args.search:
        target_packages = [ x for j in args.search for x in datase.query_regex(j) ]
        for i in target_packages:
            name, version, description = get_info(i)
            print(name, version, '\n', description)

