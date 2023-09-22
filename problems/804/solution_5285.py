def filtra_pares(tupla):
    tuplaF=()
    for elemento in tupla:
        if elemento%2==0:
            tuplaF+elemento
    return tuplaF