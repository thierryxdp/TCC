def maiores(lista,n):
    for k in range (0,len(lista)+1):
        if lista[k]<n:
            del lista[k]
            return lista