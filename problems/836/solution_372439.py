def busca(setor, matriz):
    for i in matriz:
        for j in i:
            if j == setor:
                list.remove(i, j)
            else:
                list.remove(matriz, i)
    return matriz