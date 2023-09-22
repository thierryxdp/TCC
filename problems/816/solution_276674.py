def maiores(lista,n):
    l_clone=lista[:]
    if n in lista:
        l_clone.sort()
        a,b,=l_clone[0:n-1],l_clone[n-1:]
        return b
    else:
        return lista.clear()