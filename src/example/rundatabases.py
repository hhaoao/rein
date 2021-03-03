import sys
from pathlib import Path

p = Path('../lib')
full_p = str(p.resolve())
sys.path.append(full_p)

from reindatabases import sqlite


if __name__ == "__main__":
    packages = [
        ('123','aaa'),
        ('456','ggg')
    ]
    datase = sqlite()
    datase.create_table()
    datase.packages_storage(packages)
    # test

    buckets = datase.query_regex('23')
    buckets_1 = datase.query('123')
    print(buckets)
