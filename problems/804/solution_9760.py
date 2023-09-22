def filtra_pares(filtragem):
    t1 = list(filtragem)
    for n in t1:
        if n % 2 != 0:
            t1.remove(n)
    t2 = t1
    for n in t2:
        if n % 2 != 0:
            t2.remove(n)
    t3 = tuple(t2)
    return t3