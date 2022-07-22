'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1' : randint (1,6),
        'jogador2' : randint (1,6),
        'jogador3' : randint (1,6),
        'jogador4' : randint (1,6),
        'jogador5' : randint (1,6),
        'jogador6' : randint (1,6),}
ranking = dict()

print('Os valores sorteados foram...')
for k, v in jogo.items():
    print (f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RAKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'Na colocação {i+1}º ficou o {v[0]}, que tirou {v[1]} no dado')