def filtraMultiplos(lista,n):
    l =[]
    indice= 0
    for i in lista:
        if i % n == 0:
            l.append(i)
    return l