def filtra_pares(tupla):
    for x in tupla:
        if x%2 == 0:
            tupla_par = x
        x += x
    return tupla_par