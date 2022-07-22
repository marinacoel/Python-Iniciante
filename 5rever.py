'''
quantidade de água por kg
'''
continuar = 'sim'

while continuar == 'sim':
    
    idade = int(input('\nDigite a sua idade: '))
    kg = int(input('\nDigite seu peso em kg: '))
  
    if idade <= 17:
        print(f'\nVocê deve consumir {(40 * kg)/1000:.2f} litros por dia')

    elif idade >= 18 or idade < 55:
        print(f'\nVocê deve consumir {(35 * kg)/1000:.2f} litros de água por dia')

    elif idade > 55 or idade <= 65:
        print(f'\nVocê deve consumir {(30 * kg)/1000:.2f} litros de água por dia')

    else:
        print(f'\nVocê deve consumir {(25 * kg)/1000:.2f} litros de água por dia')

    continuar = input('\nDeseja fazer outra operação? ')

print('\nObrigado!')