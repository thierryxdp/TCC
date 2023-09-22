def busca(nome,matriz):
    lista = []
    linha = len(matriz)
    for x in range(linha):
    for y in range(4):
        if nome in matriz:
            lista.append(matriz[x][y])
    return lista