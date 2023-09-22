def maiores(lista,n):
    lista.append(n)
    lista.sort()
    po = lista.index(n)
    return lista[-1:po]