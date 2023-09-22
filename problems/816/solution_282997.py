def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista.filter(maiores,n)
    return lista