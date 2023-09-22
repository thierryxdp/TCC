def faltante(l):
    f = 0
    i = max(l)
    lista = [5,1,2,3,4,90]
    while min(l) < i:
        i = i - 1
        if not i in l:
            f = i
    return f