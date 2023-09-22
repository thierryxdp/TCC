def busca(setor, matriz):
    x = 0
    for i in matriz:
        for j in i:
            if j == setor:
                list.remove(i, j)
            else:
                list.remove(matriz, matriz[x])
        x = x + 1       
    return matriz