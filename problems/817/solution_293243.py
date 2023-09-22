def acima_da_media(lista,n):
    """ """
    lista.append(n)
    lista.index(n)
    lista.sort()
    ind=lista.index(n)
    return lista[ind+1:]
    
    notas=lista
    media=n
    media=sum(notas)/len(notas)
    return media