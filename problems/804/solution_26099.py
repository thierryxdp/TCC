def filtra_pares(tupla):
    tupla_par = ()
    for x in tupla:
        if x%2 == 0:
            tupla_par += (x,)
            return tupla_par