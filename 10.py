'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep

def maior(*args):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in args:
        print(f'{valor}', end = ' ', flush = True)
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
        print(f'Foram informados {cont} valores ao todo')
        print(f'O maior valor informado foi {maior}')



maior(2, 9, 0, 5)
maior(0, 4, 5, 10)
#maior(2)