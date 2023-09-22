def maiores(lista,n):
    lista=sorted(lista)
    if lista[0]>n:
        return sorted(lista)
    if n in lista:
        return lista[n:]
    else:
        return lista[:n]