def maiores(numero,n):
    lista=numero
    if lista[0]<n:
        del lista[0]
        return lista
    if lista[1]<n:
        del lista[1]
        return lista