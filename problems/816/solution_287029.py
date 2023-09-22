def maiores(numeros,n):
    lista=sorted(numeros)
    if lista[0]<n:
        del lista[0]
        return lista+[n]