def filtra_pares(tupla):
       
    par = (t[0] % 2 == 0)

    if par:
        return 1 + pares(t[1:])
    else:
        return pares(t[1:])