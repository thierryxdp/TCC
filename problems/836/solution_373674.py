def busca(setor,matriz):
    lista_1=[]
    lista=[]
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if setor==matriz[i][j]:
                 lista.append(matriz[i])
    for i in range(nlin):
        linha=[]
        for j in range(ncol):
            if lista[i][j]!=setor:
                linha.append(lista[i][j])
        lista_1.append(linha)
    return lista_1