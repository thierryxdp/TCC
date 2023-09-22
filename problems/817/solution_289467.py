def acima_da_media(lista):
    n = sum(lista)/len(lista)
    int(n)
    lista1 = lista+[n]
    list.sort(lista1)
    posicao = list.index(lista1,n)
    return lista1[posicao+1:]