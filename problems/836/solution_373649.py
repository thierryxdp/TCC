def busca(setor,matriz):
    lista=[]
    lista_2=[]
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if setor==matriz[i][j]:
                lista.append(matriz[i])
                lista_2=lista.pop(setor)
    return lista2