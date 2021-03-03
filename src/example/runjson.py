import sys
from pathlib import Path

p = Path('../lib')
full_p = str(p.resolve())
sys.path.append(full_p)

from reinjson import ReinJson


if __name__ == "__main__":
    package = ReinJson()
    package.load('./ghostscript.json')
    if 'architecture' in package.info:
        print(package.info['architecture'].keys())
        print(package.info['checkver']['regex'])
