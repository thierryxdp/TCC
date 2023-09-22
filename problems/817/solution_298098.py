def acima_da_media(lista):
    if len(lista)=1:
        return sum(lista)
    else:
    n = sum(lista)/len(lista)
    list.insert(lista,0,n)
    list.sort(lista)
    x = list.index(lista,n)
    return lista[x+1:]