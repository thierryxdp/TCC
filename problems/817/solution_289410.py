def acima_da_media(lista):
    lista.append(lista)
    lista.sort(lista)
    lista1=lista.index(lista)
    return lista[lista1+lista.count(lista):]