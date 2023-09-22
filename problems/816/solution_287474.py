def maiores(lista,n):
    ''''''
    if n not in lista:
        list.extend(lista,[n])
    else:
        lista=lista
    Pn=list.index(lista,n)
    return lista[Pn+1:]