'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, 
mostre o conteúdo da estrutura na tela.
'''
nome: input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2)/2

if media >= 7:
    situação = 'Aprovado'
elif 5<= media < 7:
    situação = 'Recuperação'
else:
    situação = 'Reprovado'

print(f'O studante: {nome}  {situação}')