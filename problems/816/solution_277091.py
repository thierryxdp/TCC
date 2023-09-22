def maiores(lista,n):
    x=sorted(lista)
    if n in x:
        return sorted(x[:n])
    else:
        return lista[n:]