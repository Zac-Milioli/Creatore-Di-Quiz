
from system.quiz import *

# teste_quiz = Quiz('Questionario_02', [], [], [])

# teste_quiz.add_pergunta('Primeiro teste', '00645')
# teste_quiz.add_pergunta('Segundo', '154')
# teste_quiz.add_pergunta('Lorem ipsum sla oq sla oq teste teste string longa compridona teste teste aooooooooooo', '18765')
# teste_quiz.add_pergunta('Mario', '054841')

# teste_quiz.ver_quiz()

# teste_quiz.save_quiz()

teste_carregar = load_quiz('system/Quiz&Questionario_02&.csv')

print(teste_carregar.get_id())
print(teste_carregar.get_perguntas())


teste_carregar.ver_quiz()
