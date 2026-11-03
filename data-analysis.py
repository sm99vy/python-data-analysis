pessoas = []
dado = []
mais_pesados = []
mais_leves = []

print('Cadastro de pessoas e seus pesos')

while True:
    dado.append(str(input('Por favor, digite o nome: ')).strip())
    dado.append(float(input('Agora, digite o peso (KG): ')))
    pessoas.append(dado[:])
    dado.clear()

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

mais_pesados = pessoas[:]
mais_leves = pessoas[:]
rodada_atual = 0

while rodada_atual < len(mais_pesados):
    posicao_atual = 0
    while posicao_atual < len(mais_pesados) - 1:
        if mais_pesados[posicao_atual][1] < mais_pesados[posicao_atual + 1][1]:
            pessoa_temporaria = mais_pesados[posicao_atual]
            mais_pesados[posicao_atual] = mais_pesados[posicao_atual + 1]
            mais_pesados[posicao_atual + 1] = pessoa_temporaria
        posicao_atual += 1
    rodada_atual += 1
rodada_atual = 0

while rodada_atual < len(mais_leves):
    posicao_atual = 0
    while posicao_atual < len(mais_leves) - 1:
        if mais_leves[posicao_atual][1] > mais_leves[posicao_atual + 1][1]:
            pessoa_temporaria = mais_leves[posicao_atual]
            mais_leves[posicao_atual] = mais_leves[posicao_atual + 1]
            mais_leves[posicao_atual + 1] = pessoa_temporaria
        posicao_atual += 1
    rodada_atual += 1

print(f'\nForam cadastradas {len(pessoas)} pessoas.')
print('\nLista do mais pesado para o mais leve:')
for pessoa in mais_pesados:
    print(f' - {pessoa[0]} com {pessoa[1]} KG')
print('\nLista do mais leve para o mais pesado:')
for pessoa in mais_leves:
    print(f' - {pessoa[0]} com {pessoa[1]} KG')