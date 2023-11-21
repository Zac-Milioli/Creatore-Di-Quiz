from system.system_prepare import *

class Quiz:
    def __init__(self, nome: str, perguntas: list, id: list, respostas: list):
        self.nome = nome
        self.perguntas = perguntas
        self.id = id
        self.respostas = respostas

    def ver_quiz(self):
        tabela = Table(title=f'[bright_yellow]Quiz {self.nome}')
        tabela.add_column('ID', justify='center', style='bright_cyan')
        tabela.add_column('Perguntas', justify='left', style='bright_green')
        for i in range(0, len(self.id)):
            tabela.add_row(self.id[i], self.perguntas[i])
        console.print(tabela)
        return tabela

    def get_perguntas(self):
        return self.perguntas
    
    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_respostas(self):
        return self.respostas

    def save_quiz(self):
        df = pd.DataFrame({'ID': self.id, 'Perguntas': self.perguntas})
        try:
            df.to_csv(f'system/Quiz&{self.get_nome()}&.csv', sep=';')
            print(f'[bright_yellow]system/Quiz&{self.get_nome()}&.csv CRIADO')
        except:
            print(f'[bright_red]AVISO: não foi possível salvar o arquivo.\nVerifique o formato:[/bright_red]\n{self.ver_quiz()}\n{df}\n')

    def add_pergunta(self, pergunta:str, codigo:int):
        try:
            self.perguntas.append(pergunta)
            self.id.append(codigo)
            print(f'[bright_blue]Pergunta adicionada com sucesso')
        except:
            print(f'[bright_red]Não foi possível salvar a pergunta')

    def add_resposta(self, resposta):
        try:
            self.respostas.append(resposta)
            print(f'[bright_blue]Resposta gravada com sucesso')
        except:
            print(f'[bright_red]Não foi possível salvar a resposta')

    def remover_pergunta(self, idx):
        if idx in self.id:
            local = self.id.index(idx)
            self.perguntas.pop(local)
            self.id.pop(local)
            try:
                self.respostas.pop(local)
            except:
                pass
            print(f'[bright_yellow]Removeu pergunta com sucesso')
        else:
            print(f'[bright_red]ID[/bright_red] [cyan]{idx}[/cyan] [bright_red]não encontrado na lista de IDs[/bright_red]')

def load_quiz(csv:str):
    loaded = pd.read_csv(csv, sep=';')
    quiz_name = csv.split('&')[1]
    questions = []
    ids = []
    for i in loaded.index:
        ids.append(str(loaded.at[i, 'ID']))
        questions.append(loaded.at[i, 'Perguntas'])
    loaded_quiz = Quiz(nome=quiz_name, perguntas=questions, id=ids, respostas=[])
    print(f'[bright_yellow]{csv} CARREGADO')
    return loaded_quiz
