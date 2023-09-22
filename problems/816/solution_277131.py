def maiores(lista,n):
    lista=sorted(lista)
    if n in lista:
        return n
    else:
        return lista[n:]