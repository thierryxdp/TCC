def busca(setor, matriz):
    #workers = []
    for i in range(len(matriz)):
        if matriz[i][1] == setor:
            return matriz[i]