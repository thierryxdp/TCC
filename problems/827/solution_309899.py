def qtd_divisores (n):
    a = list(range(n+1))
    list.remove (a, 0)
    r = 0
    for e in a:
        if n % e == 0:
            r = r+1
        else:
            r = r
    return r