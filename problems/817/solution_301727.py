def acima_da_media(lista):
    m = sum(lista)/len(lista)
    list.insert(lista, m)
    list.sort(lista)
    i = list.index(lista, m)
    return lista[i+1:]