def filtra_pares(tup):
    resul = ()
    par_a = tup[0]%2==0
    par_b = tup[1]%2==0
    par_c = tup[2]%2==0
    par_d = tup[3]%2==0
    if int(par_a) and int(par_b) and int(par_c) and int(par_d) == 1:
        return resul + tup[:]