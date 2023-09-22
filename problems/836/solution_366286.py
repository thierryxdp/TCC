def busca(informacao, matriz):
    setor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str.count(informacao,matriz[i][j])>0:
                setor += (matriz[i][0:j] + [matriz[i][j + 1]],)
    return setor