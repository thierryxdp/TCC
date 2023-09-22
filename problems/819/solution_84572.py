def filtraMultiplos(lista, m):
    for elemento in lista:
        if elemento%m==0:
            return tuple(elemento)