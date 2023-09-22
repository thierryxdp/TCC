def filtra_pares(tupla):
    copia=()
    for x in tupla:
        if x%2==0:
            copia=copia+tuple(x)
    return copia