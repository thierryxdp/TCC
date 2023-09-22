def acima_da_media(lista):
    a = sum(lista)
    c = len(lista)
    b = a/c
    list = lista
    list.append(b)
    list.sort()
    return list[(list.index(b)+1):]