def filtraMultiplos(lista,n):
    mult = []
    for i in lista:
        if i%n == 0:
            mult.append(i)
    return mult