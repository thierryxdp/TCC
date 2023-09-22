def maiores(lista,n):
    ''''''
    if n not in lista:
        list.extend(lista,[n])
    else:
        lista=lista
    list.sort(lista)    
    Pn=list.index(lista,n)
    return lista[Pn+1:]