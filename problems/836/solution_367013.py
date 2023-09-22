def busca(setor,matriz):
    for i in range(len(matriz)):
        if setor not in matriz[i][2]:
            del matriz[i]
            lista+=[matriz]
            del lista[i][2]
            i+=0
            return lista