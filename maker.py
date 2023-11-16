# Feito para criar os questionários

from system.system_prepare import *
clear_screen()
menu = True

while menu:
    title_print()
    separators()
    print('\nSelecione alguma opção:\n\n[0] [bright_red]Salvar e sair[/bright_red]\n[[bright_cyan]ENTER[/bright_cyan]] [bright_red]Sair sem salvar[/bright_red]\n')
    separators()
    opt = input('\n...')
    if opt == '0':
        clear_screen()
        menu = False
    elif opt == '':
        clear_screen()
        menu = False
    elif opt == '1':
        clear_screen()
    elif opt == '2':
        clear_screen()
    elif opt == '3':
        clear_screen()
    elif opt == '4':
        clear_screen()
    elif opt == '5':
        clear_screen()
    elif opt == '6':
        clear_screen()
    elif opt == '7':
        clear_screen()
    elif opt == '8':
        clear_screen()
    else:
        clear_screen()
        print('[bright_red]Selecione uma opção válida\n\n')
        clear_screen()

roll_credits()
