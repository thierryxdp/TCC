def maiores(lista,n):
    lista=sorted(lista)
    if n not in lista:
        return lista
    if n in lista:
        return lista[n:]
    else:
        return lista[:n]