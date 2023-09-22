def acima_da_media(lista):   
    a=sum(lista)
    b=a/len(lista)
    list.append(lista,b)
    list.sort(lista)
    c=list.index(lista,b)
    if b in lista:
        return lista[c+1:]
    else:
        return lista