def maiores(lista,n):
    lista=sorted(lista)
    if lista>n:
        return lista[n:]