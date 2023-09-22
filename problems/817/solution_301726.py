def acima_da_media(lista):
    m = sum(lista)/len(lista)
    i = list.index(lista, m)
    return lista[i:]