def filtra_pares(tupla):
    for tupla[0:1] in tupla:
        if tupla[0:1] % 2 == 0:
            return tupla[0:1]