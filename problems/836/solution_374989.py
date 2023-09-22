def busca(setor,matriz):
    aliase = []
    for i in range(len(matriz)):
            if setor == matriz[i][2]:
                aliase += matriz[i]
                del aliase[2]
    return aliase