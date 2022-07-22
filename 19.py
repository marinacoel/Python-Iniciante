'''
Somar os valores do carrinho
'''

carrinho = []

carrinho.append(('Produto 1', 90))
carrinho.append(('Produto 2', 60))
carrinho.append(('Produto 3', 120))

total = sum([float(y) for x, y in carrinho])
print(total)
