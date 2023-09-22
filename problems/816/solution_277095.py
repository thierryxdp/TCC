def maiores(lista,n):
    x=sorted(lista)
    if n in x:
        return x
    else:
        return lista[n:]