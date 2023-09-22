def filtraMultiplos(lista,n):
    div = []
    for x in lista:
        if x % n == 0:
            div.append(x)
    return div