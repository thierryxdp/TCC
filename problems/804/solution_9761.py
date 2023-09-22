def filtra_pares(filtragem):
    t1 = list(filtragem)
    for n in t1:
        if n % 2 != 0:
            t1.remove(n)
    t2 = t1
    for n in t2:
        if n % 2 != 0:
            t2.remove(n)
    t3 = t2
    for n in t3:
        if n % 2!= 0:
            t3.remove(n)
    t4 = tuple(t3)
    return t4