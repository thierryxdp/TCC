def maiores(lista,n):
    if lista[0]>n:
        return sorted(lista)
    if lista[6]>n:
        return lista[6]
    else:
        return lista[n:]