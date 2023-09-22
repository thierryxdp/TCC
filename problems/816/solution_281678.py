def maiores(lista,n):
    a = max(lista)
    b = lista.pop(a)
    c = max(b)
    if c>n:
        return c+a