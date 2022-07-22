'''
Receba os valores em uma lista e dobre cada um deles
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*= 2
        pos += 1

valores = [1, 2, 8, 7, 0,]

dobra(valores)
print(valores)