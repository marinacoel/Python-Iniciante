'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.
'''

def ficha(nome = '<desconhecido>', gol = 0):
    print(f'O jogador {nome} fez {gol} gols no campeonato.')

n = str(input('Digite o nome do jogador :'))
g = input('Digite a quantidade de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gol = g)
else:
    ficha(n, g)
