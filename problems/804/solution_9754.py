def filtra_pares(filtragem):
    t1 = list(filtragem)
    n1,n2,n3,n4 = t1
    for n in t1:
        if n % 2 != 0:
            t1.remove(n)
    t2 = tuple(t1)
    return t2