def busca(setor, matriz):
    nlinhas = len(matriz)
    linha = []
    for i in range(nlinhas):
        if matriz[i][2] == setor:
            linha.append(matriz[i].remove(setor))
    return linha