def busca(setor,matriz):
    for i in range(len(matriz)):
        if matriz[i].count(setor)==0:
            del matriz[i]
            del matriz[i][2]
            i+=0
        return matriz