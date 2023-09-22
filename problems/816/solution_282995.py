def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista.filter(n,lista)
    return lista