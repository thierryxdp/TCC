def filtraMultiplos(lista, m):
    matue= []
    for elemento in lista:
        if elemento%m==0:
            matue.append(elemento)
    return matue