def busca(setor,matriz):
    lista_1=[]
    lista=[]
    lista_2=[]
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if setor==matriz[i][j]:
                 lista.append(matriz[i])
            if setor in matriz[i][j]:
                p=matriz.index(setor)
                if setor==matriz[i][j]:
                    del(matriz[p])
    return matriz