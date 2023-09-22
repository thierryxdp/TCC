def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista.filter(lista,n)
    return lista