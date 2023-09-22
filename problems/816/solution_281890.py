def maiores(lista,n):
    list.sort(lista)
    list.insert(lista,n,0)
    n=lista[0]
    x=lista[1:]
    return x>n