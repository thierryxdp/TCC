def busca(setor,matriz):
    for i in range(len(matriz)):
        for setor in matriz[i][2]:
            i+=1
        return matriz[i]