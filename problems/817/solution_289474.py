def acima_da_media(lista):
    n = sum(lista)/len(lista)
    lista1 = lista+[int(n)]
    list.sort(lista1)
    posicao = list.index(lista1,int(n))
    return lista1[posicao+1:]