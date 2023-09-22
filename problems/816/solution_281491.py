def maiores(lista,n):
    if n in lista:
        list.sort(lista)
        del lista[:n]
        return lista