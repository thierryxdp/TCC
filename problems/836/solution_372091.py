def busca(setor,matriz):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    linha = []
    for i in range(nlinhas):
        for j in range(ncolunas):
            if matriz[i][j] == setor:
                linha.append(matriz[i].remove(setor))
    return linha