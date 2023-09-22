def filtra_pares(tupla):
    tupla_par = ()
    for n in tupla:
        if n%2 == 0:
            tuple(tupla_par) + tuple(n,)
    return tupla_par