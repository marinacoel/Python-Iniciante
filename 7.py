'''
Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def area (a, b):
    tam = a * b
    print(f'A área de um terreno de {a} x {b} é {tam:.2f}m².')
 
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)