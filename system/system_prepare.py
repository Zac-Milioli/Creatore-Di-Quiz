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
from rich.console import Console
from rich.table import Table
from system.quiz import *
from system.quiz_dep import *
console = Console()
install()

clear_screen = lambda: print('\n'*100)
separators = lambda: print('>'*60)
title_print = lambda: print('[bright_cyan]█▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀█ █▀█ █▀▀   █▀▄ █   █▀█ █ █ █ ▀█\n█▄▄ █▀▄ ██▄ █▀█  █  █▄█ █▀▄ ██▄   █▄▀ █   ▀▀█ █▄█ █ █▄')

def roll_credits():
    title_print()
    separators()
    print('\n[bright_green]Obrigado por usar![/bright_green]\n\nFeito por [bright_yellow]Zac Milioli[/bright_yellow]\n-\thttps://www.linkedin/in/zac-milioli\n-\thttps://github.com/Zac-Milioli\n-\t[bright_blue][underline]zacmilioli@gmail.com[/underline][/bright_blue]\n')
    separators()
