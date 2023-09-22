def maiores(lista,n):
    list.insert(lista,0,n)
    list.sort(lista)
    nyx=lista[list.index(lista,n):]
    list.remove(nyx,n)
    return nyx