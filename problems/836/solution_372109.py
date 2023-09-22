def busca(setor, matriz):
    nlinhas = len(matriz)
    linha = []
    for i in range(nlinhas):
        for j in range(4):
            if matriz[i][j] == setor:
                linha.append(matriz[i].remove(setor))
    return linha