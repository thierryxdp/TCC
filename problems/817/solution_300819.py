def acima_da_media(lista):
    a = sum(lista)/len(lista)
    list.sort(lista)
    lista = lista[list.index(lista,a):]
    return lista