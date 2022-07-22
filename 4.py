'''
Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
'''
def fb(n):
    if n % 5 == 0 and n % 3 == 0:
        return f'fizzbuzz! o numero {n} é divisivel por 3 e 5'
    if n % 3 == 0:
        return f'fizz! o numero {n} é divisivel por 3'
    if n % 5 == 0:
        return f'buzz! o numero {n} é divisivel por 5'
    return n

from random import randint
for p in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))


