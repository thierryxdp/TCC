def acima_da_media(lista):
    lista.append(lista)
    lista.sort()
    lista1=lista.index(n)
    return lista[lista1+lista.count(lista):]