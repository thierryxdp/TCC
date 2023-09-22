def busca(setor,matriz):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    linha = []
    for i in range(nlinhas):
        if matriz[i][2] == setor:
                linha.append(matriz[i].remove(setor))
    return linha