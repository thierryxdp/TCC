def maiores(lista,n):
    x=sorted(lista)
    if n in x:
        lista=lista[n:]
        return lista