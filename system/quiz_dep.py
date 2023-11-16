from system.system_prepare import *

class QuizDep(Quiz):
    def __init__(self, type):
        self.type = 'QuizDep'

def load_quiz(csv:str):
    loaded = pd.read_csv(csv, sep=';')
    quiz_name = csv.split('&')[2]
    questions = []
    ids = []
    for i in loaded.index:
        ids.append(str(loaded.at[i, 'ID']))
        questions.append(loaded.at[i, 'Perguntas'])
    loaded_quiz = QuizDep(nome=quiz_name, perguntas=questions, id=ids, respostas=[])
    print(f'[bright_yellow]{csv} CARREGADO')
    return loaded_quiz