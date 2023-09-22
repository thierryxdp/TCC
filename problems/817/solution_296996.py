def acima_da_media(lista):
    a=sum(lista)
    b=a/len(lista)
    list.append(lista,b)
    list.sort(lista)
    c=list.index(lista,b)
    d=lista[c+1]
    if b in lista:
        return d
    else:
        return d