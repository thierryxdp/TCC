def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista=[lista.index(n),]
    return lista