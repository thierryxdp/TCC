def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            lista+=[matriz[i]]
            i+=1
            for j in range(len(lista)):
                del lista[j][2]
        return lista