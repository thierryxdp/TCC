def busca(informacao, matriz):
    setor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str.count(informacao,matriz[i][j])>0:
                setor += list.remove(matriz[i],matriz[i][j])
    return setor