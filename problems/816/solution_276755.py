def maiores(lista,n):
    if lista[0]>n:
        return sorted(lista)
    if lista[1]>n:
        return sorted(lista)
    if lista[2]>n:
        return sorted(lista)
    if lista[6]>n:
        return sorted(lista)
    else:
        return lista[n:]