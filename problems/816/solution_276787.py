def maiores(lista,n):
    if lista[0]>n:
        return sorted(lista)
    if n>lista[1]:
        return sorted(lista)
    else:
        return lista[n:]