def filtra_pares(tupla):
       
    par = (tupla[0] % 2 == 0)

    if par:
        return 1 + pares(t[1:])
    else:
        return pares(t[1:])