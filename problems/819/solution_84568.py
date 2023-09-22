def filtraMultiplos(lista, m):
    resultado= 0
    for elemento in lista:
        if elemento%m==0:
            resultado=resultado+elemento
    return resultado