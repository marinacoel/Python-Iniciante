"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.   #condição: não pode somar com 0
"""

def funcao(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        return
    return n1 + n2 + n3

resultado = funcao(9, 5, 0)

if resultado:
    print(resultado)
else:
    print('não quero somar com 0!')