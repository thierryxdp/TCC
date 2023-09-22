def maiores(lista,n):
    if lista[1]>n:
        return sorted(lista)
    else:
        return lista[n:]