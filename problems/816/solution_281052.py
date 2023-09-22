def maiores(lista,n):
    if n in lista:
        lista.sort()
        return lista[lista.index(n):]