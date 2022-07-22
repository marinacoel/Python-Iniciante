'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
def voto(a):
    from datetime import date
    from time import sleep
    hoje = date.today().year
    
    idade = hoje - a
    if idade >= 18 and idade <= 65:
    
        print('\nSua idade é...\n', flush= True)
        sleep(0.5)
        print(f'{idade}: VOTO OBRIGATÓRIO\n')
    elif hoje - a < 16:
        print('\nSua idade é...\n', flush= True)
        sleep(0.5)
        print(f'{idade}: VOTO NEGADO\n')
    else:
        print('\nSua idade é...\n', flush= True)
        sleep(0.5)
        print(f'{idade}: VOTO OPCIONAL\n')
    

n = int(input('\nDigite seu ano de nascimento: '))
voto(n)

