def busca(setor, matriz):
    workers = []
    for i in range(len(matriz)):
        print(matriz[i], matriz[i][1])
        if matriz[i][1] == setor:
            return matriz[i]