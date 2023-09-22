def busca(setor,matriz):
    for i in range(len(matriz)):
        if setor not in matriz[i][2]:
            matriz1=del matriz[i]
            del matriz1[i][2]
            i+=0
            return matriz1