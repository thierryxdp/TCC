def maiores(lista,n):
    lista.append(n)
    lista.sort()
    x=lista.index(n)
    return lista[x+1:]