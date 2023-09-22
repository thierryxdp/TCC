def filtra_pares(filtragem):
    t1 = list(filtragem)
    for n in t1:
        if n % 2 != 0.00000:
            t1.remove(n)
    t2 = tuple(t1)
    return t2