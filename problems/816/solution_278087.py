def maiores(lista,n):
    novalista=lista+[n]
    list.sort(novalista)
    posicao_n=list.index(novalista,n)
    listafinal=novalista[posicao_n:]
    return listafinal