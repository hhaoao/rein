import sys
from pathlib import Path

p = Path('../lib')
full_p = str(p.resolve())
sys.path.append(full_p)

from reinpath import find_bucket_path


if __name__ == "__main__":
    buckets = find_bucket_path('../buckets')
    print(buckets)
