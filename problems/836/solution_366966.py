def busca(setor,matriz):
    lista=[]
    i=0
    while i <len(matriz):
        if setor in matriz[i][2]:
            lista+=[matriz[i]]
            i+=0
            for j in range(len(lista)):
                del lista[j][2]
        return lista