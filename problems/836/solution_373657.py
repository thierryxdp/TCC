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
                    
    return lista