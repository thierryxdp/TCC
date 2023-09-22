def filtraMultiplos (x):
    lista = []
    i = 1
    while i <= x:
        if x % i == 0:
            lista.append(i)
    i = x - 1
    return lista