"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""

def funcao(n1, n2):
    if n2:
        n2 = n2 / 100
        return n1 + (n1 * n2)

funcao(10, 10)
print (funcao)
funcao(0, 10)
print(funcao)
funcao(9, 100)
print(funcao)

