def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        if matriz[i].count(setor) > 0:
            del matriz[i][2]
            lista+=[matriz[i]]
            i+=0
            return lista