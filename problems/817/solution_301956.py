def acima_da_media(lista):
    list.sort(lista)
    a = len(int(sum(lista)/len(lista)))
    p = list.index(lista,a)
    return lista[p:]