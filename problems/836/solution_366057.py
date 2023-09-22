def busca(informacao, matriz):
    setor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            for j not in list.index(matriz[i],informacao):
                if str.count(informacao,matriz[i][j])>0:
                    setor += matriz[i],
    return setor