def filtraMultiplos(lista, m):
    cu= []
    for elemento in lista:
        if elemento%m==0:
            cu=cu+elemento
    return cu