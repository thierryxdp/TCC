def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            lista+=[matriz[i]]
            i+=1
            lista.remove(setor)
        return lista