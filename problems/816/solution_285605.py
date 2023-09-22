def maiores(lista,n):
    list.insert(lista,0,n)
    list.sort(lista)
    nyx=lista[list.index(lista,n):]
    del(nyx,n)
    return lista