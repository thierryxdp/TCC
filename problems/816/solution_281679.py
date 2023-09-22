def maiores(lista,n):
    a = max(lista)
    b = list.pop(lista,a)
    c = max(b)
    if c>n:
        return c+a