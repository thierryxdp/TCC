def filtraMultiplos(lista,n):
    l =[]
    for i in lista:
        if i % n == 0:
            l.append(i)
            return l
        else: