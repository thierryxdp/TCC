def acima_da_media(lista):
    n = sum(lista)/len(lista)
    if n in lista:
        list.sort(lista)
        a = list.index(lista,n)
        return lista[a+1:]
    if n not in lista:
        list.append(lista,n)
        list.sort(lista)
        a = list.index(lista,n)
        return lista[a+1:]