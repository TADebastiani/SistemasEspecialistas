from Diagnostico import *
from Perguntas import *

# Inferência
se = Diagnostico()
perguntas = Perguntas()

while se.probabilidade() != 100:
    pergunta = perguntas.proxima()
    se.pergunta(pergunta[0], pergunta[1])
    #print('probabilidade é %d' % (se.probabilidade()))
    print(se.db)
    print(se.resultado)
    if se.probabilidade() == 100:
        print('O motivo do dispositivo de proteção do motor ter atuado é : ', se.resultado[0])
