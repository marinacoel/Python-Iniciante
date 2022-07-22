'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep

def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'\nContar de {inicio} ao {fim}, pulando de {passo} em {passo}')

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim: 
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end = '-', flush= True )
            cont += passo
            sleep(0.5)
        print('\nFIM!\n')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end = '-', flush= True)
            cont -= passo
            sleep(0.5)
        print('Fim!\n')


contador(0, 100, 20)
contador(10, 2, 1)

print('-=' *20)
print('\nAgora é sua vez de personalizar a contagem!\n')
i = int(input('Digite o início: '))
f= int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

contador(i, f, p)




