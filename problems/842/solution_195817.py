def pontos_por_time(lista):
    dicionario = {}
    for x in lista:
        nome_1, nome_2, placar = x
        if placar[0] == placar[1]:
            dicionario[x[0]] += 1
            dicionario[x[1]] += 1
        elif placar[0] > placar[1]:
            dicionario[nome_1] += 3
        elif placar [0] < placar[1]:
            dicionario[nome_2] += 3
    return  dicionario