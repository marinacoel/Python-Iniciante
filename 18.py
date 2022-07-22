'''
Separar uma lista com numeros repetidos (list comprehension)
string = '01234567890123456789012345678901234567890123456789'
retorno = '0123456789.0123456789.0123456789.0123456789.0123456789'
'''

variavel = '01234567890123456789012345678901234567890123456789'
n = 10
lista = [variavel[i:i + n] for i in range(0, len(variavel), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)