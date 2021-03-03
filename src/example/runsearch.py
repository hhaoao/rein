import sys
from pathlib import Path

p = Path('../lib')
full_p = str(p.resolve())
sys.path.append(full_p)

from reinpath import search_packages

if __name__ == "__main__":
    files_stem = search_packages(['__init__'], './', '**/*.py')
    for i in files_stem:
        print(i)

