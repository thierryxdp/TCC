def acima_da_media(lista):
    n = sum(lista)/len(lista)
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    if n in lista:
        return lista[a+2:]
    else:
        return lista[a+1:]