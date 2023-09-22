def maiores(lista,n):
    x=list.sort(lista)
    if n in x:
        return x
    if not n in x:
        return x[:n]