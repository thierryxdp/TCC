def maiores(lista,n):
    if len(lista)>n:
        return sorted(lista)
    else:
        return lista[n:]