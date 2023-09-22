def maiores(lista,n):
    if n in lista:
        lista=sorted(lista)
        del lista[0:n]
        return lista