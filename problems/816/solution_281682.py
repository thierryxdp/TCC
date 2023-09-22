def maiores(lista,n):
    a = max(lista)
    b = lista.reverse()
    c = list.pop(1)
    d = max(c)
    if d>n:
        return d+a