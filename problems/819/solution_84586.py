def filtraMultiplos(lista, m):
    cu= []
    for elemento in lista:
        if elemento%m==0 and m in lista:
            cu=cu+list.append(elemento, m)
        elif elemento%m==0 and m not in lista:
            cu=cu+elemento
        else:
            cu=cu
    return cu