dados = dict()
partidas = list()
dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou?'))
for c in range(0, partidas):
    partidas(int(input(f'      Quantos gols ele fez na partida {c}?')))
dados['Gols'] = partidas[:]
dados['Total'] = sum(partidas)
print('=-' * 30)
print(dados)
print('=-' * 30)
