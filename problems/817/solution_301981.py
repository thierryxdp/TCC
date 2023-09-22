def acima_da_media(lista):
    n = sum(lista)/len(lista)
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    if len(lista)<=1:
        return []
    else:
        return lista[int(a)+1:]