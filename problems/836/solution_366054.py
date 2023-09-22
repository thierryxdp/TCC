def busca(informacao, matriz):
    setor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str.count(informacao,matriz[i][j])>0:
                setor += str.remove(matriz[i][j],2)
    return setor