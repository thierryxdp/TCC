def filtra_pares(t1,t2,t3,t4):
    tupla = [t1,t2,t3,t4]
    for i, n in enumerate(tupla):
        if n % 2 == 0:
            tupla.append(i)
    return tupla