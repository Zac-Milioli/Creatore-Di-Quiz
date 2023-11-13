# Feito para criar os questionários

from system.system_prepare import *
clear_screen()
menu = True
quiz = pd.read_csv(r'system/quiz.csv', sep=';')
quiz_dep = pd.read_csv(r'system/quiz&dep.csv', sep=';')

while menu:
    title_print()
    separators()
    print('\nSelecione alguma opção:\n\n[1] [green]Criar[/green] um novo questionário\n[2] [green]Criar[/green] um novo questionário de dependências\n\n[3] [green]Editar[/green] alguma pergunta do questionário a partir de seu index\n[4] [green]Editar[/green] alguma pergunta do questionário de dependências a partir de seu index\n\n[5] [green]Ver[/green] o questionário atual\n[6] [green]Ver[/green] o questionário de dependências atual\n\n[7] [green]Excluir[/green] o questionário atual\n[8] [green]Excluir[/green] o questionário de dependências atual\n\n\n\n[0] [bright_red]Salvar e sair[/bright_red]\n[[bright_cyan]ENTER[/bright_cyan]] [bright_red]Sair sem salvar[/bright_red]\n')
    separators()
    opt = input('\n...')
    if opt == '0':
        clear_screen()
        quiz.loc[:, ~quiz.columns.str.match('Unnamed')].to_csv(r'system/quiz.csv', sep=';')
        quiz_dep.loc[:, ~quiz_dep.columns.str.match('Unnamed')].to_csv(r'system/quiz&dep.csv', sep=';')
        print('[yellow]quiz.csv salvo')
        print('[yellow]quiz&dep.csv salvo\n\n')
        menu = False
    elif opt == '':
        clear_screen()
        menu = False
    elif opt == '1':
        clear_screen()
        creating = True
        ans = {'pergunta': [], 'id': []}
        while creating:
            print('[blue][bold]\t\tCRIAÇÃO DE QUESTIONÁRIO')
            separators()
            print('\n[1] [bright_green]Adicionar[/bright_green] pergunta\n\n[0] [blue]Salvar e sair[/blue]\n[[bright_cyan]ENTER[/bright_cyan]] [bright_red]Sair sem salvar[/bright_red]\n')
            separators()
            escolha = input('\n...')
            clear_screen()
            if escolha == '1':
                print('\nSim funciona\n')
            elif escolha == '':
                creating = False
            elif escolha == '0':
                if len(ans['pergunta']) == 0:
                    print('[bright_red]AVISO: não é possível criar questionário vazio\n')
                else:
                    quiz = pd.DataFrame([ans])
                    creating = False
        clear_screen()
    elif opt == '2':
        clear_screen()
        creating = True
        ans = {'pergunta': [], 'id': []}
        while creating:
            print('[blue][bold]\t\tCRIAÇÃO DE QUESTIONÁRIO')
            separators()
            print('\n[1] [bright_green]Adicionar[/bright_green] pergunta\n\n[0] [blue]Salvar e sair[/blue]\n[[bright_cyan]ENTER[/bright_cyan]] [bright_red]Sair sem salvar[/bright_red]\n')
            separators()
            escolha = input('\n...')
            clear_screen()
            if escolha == '1':
                print('\nSim funciona\n')
            elif escolha == '':
                creating = False
            elif escolha == '0':
                if len(ans['pergunta']) == 0:
                    print('[bright_red]AVISO: não é possível criar questionário vazio\n')
                else:
                    quiz_dep = pd.DataFrame([ans])
                    creating = False
        clear_screen()
    elif opt == '3':
        clear_screen()
        print('[blue][bold]\t\tEDIÇÃO DE QUESTIONÁRIO')
        separators()
        clear_screen()
    elif opt == '4':
        clear_screen()
        print('[blue][bold]\t\tEDIÇÃO DE QUESTIONÁRIO')
        separators()
        clear_screen()
    elif opt == '5':
        clear_screen()
        quiz_table = Table(title='Questionário Atual')
        quiz_table.add_column('index', justify='center', style='bright_magenta')
        quiz_table.add_column('Pergunta', justify='left', style='bright_green')
        quiz_table.add_column('ID', justify='right', style='bright_yellow')
        for i in quiz.index:
            pergunta = quiz.at[i, 'pergunta']
            codigo = quiz.at[i, 'id']
            quiz_table.add_row(i, pergunta, codigo)
        console.print(quiz_table)
        print('\n\nPressione [bright_red]ENTER[/bright_red] para retornar ao menu\n')
        input()
        clear_screen()
    elif opt == '6':
        clear_screen()
        quiz_table = Table(title='Questionário de Dependências Atual')
        quiz_table.add_column('index', justify='center', style='bright_magenta')
        quiz_table.add_column('Pergunta', justify='left', style='bright_green')
        quiz_table.add_column('ID', justify='right', style='bright_yellow')
        for i in quiz_dep.index:
            pergunta = quiz_dep.at[i, 'pergunta']
            codigo = quiz_dep.at[i, 'id']
            quiz_table.add_row(i, pergunta, codigo)
        console.print(quiz_table)
        print('\n\nPressione [bright_red]ENTER[/bright_red] para retornar ao menu\n')
        input()
        clear_screen()
    elif opt == '7':
        clear_screen()
        quiz = pd.DataFrame(columns=['pergunta', 'id'])
        quiz.loc[:, ~quiz.columns.str.match('Unnamed')].to_csv(r'system/quiz.csv', sep=';')
        print('[yellow]quiz.csv limpo\n\n')
    elif opt == '8':
        clear_screen()
        quiz_dep = pd.DataFrame(columns=['pergunta', 'id'])
        quiz_dep.loc[:, ~quiz_dep.columns.str.match('Unnamed')].to_csv(r'system/quiz&dep.csv', sep=';')
        print('[yellow]quiz&dep.csv limpo\n\n')
    else:
        clear_screen()
        print('[bright_red]Selecione uma opção válida\n\n')
        clear_screen()

roll_credits()
