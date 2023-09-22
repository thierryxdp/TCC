def busca(setor,matriz):
    nlinhas = len(matriz)
    linha = []
    for i in range(nlinhas):
        if setor in matriz[i]:
            linha.append(matriz[i].remove(setor))
    return linha