def filtraMultiplos(lista, n):
    ret = []
    for i in lista:
        if i%n==0:
            ret.append(i)
    return(ret)