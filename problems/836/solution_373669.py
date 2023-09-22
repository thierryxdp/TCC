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
    for i in range(nlin)
         matriz[i][j]=matriz.index(setor)
         del(matriz[i][j])
    return matriz