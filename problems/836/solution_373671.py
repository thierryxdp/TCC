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
         for j in range(ncol):
            if lista[i][j]!=setor:
                lista_1.append(lista[i][j])
                lista_1.append(lista)
    return lista    
              
    return matriz