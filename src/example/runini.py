import sys
from pathlib import Path

p = Path('../lib')
full_p = str(p.resolve())
sys.path.append(full_p)

from reinini import read_ini 


if __name__ == "__main__":
    config = read_ini('rein.ini')
    print(config['rein']['system'])
