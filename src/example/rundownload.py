import sys
from pathlib import Path

p = Path('../lib')
full_p = str(p.resolve())
sys.path.append(full_p)

from reindownload import ReinDownload


if __name__ == "__main__":
    package = ReinDownload()
    url_list = ['http://example.org/file']
    package.add_urls(url_list)
    print('完成')
