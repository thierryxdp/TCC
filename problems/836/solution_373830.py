def busca(setor,matriz):
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            return matriz[i][2]