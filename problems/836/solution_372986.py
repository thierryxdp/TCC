def busca(matriz,setor):
    ''' '''
    retorno=[]
    for i in matriz:
        for j in i:
            if j==setor:
                y=list.index(i,j)
                del i[y]
                retorno+=[i,]
    return retorno