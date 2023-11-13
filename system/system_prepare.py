# Atualiza e instal os pacotes necessários

import os

with open(r'system/has_setup.txt', 'r') as setup:
    if setup.read() == '0':
        os.system('python -m pip install --upgrade pip')
        os.system('pip install --upgrade python')
        os.system('pip install pandas')
        os.system('pip install rich')
        open(r'system/has_setup.txt', 'w').write('1')


import pandas as pd
from rich.traceback import install
from rich import print
install()
