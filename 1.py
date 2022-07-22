"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""

def saudacao (s1 = 'oi', s2 = 'seu nome'):
    s1 = s1.replace('a', 'A')
    s2 = s2.replace('a', 'A').replace('i', 'I')
    print (s1, s2)

saudacao('Ola', 'Marina')
saudacao(s2 = 'Joao')
saudacao()

