def maiores(lista,n):
    n=sorted(lista)
    if n in lista:
        return lista[n:]
    else:
        return [:n]