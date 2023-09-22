def filtra_pares(tup):
    tup = ('a', 'b', 'c', 'd')
    par_a = tup[0]%2
    par_b = tup[1]%2
    par_c = tup[2]%2
    par_d = tup[3]%2
    if par_a and par_b and par_c and par_d == True:
        return str(tup[:])
    elif int(par_a) and int(par_b) and int(par_c) == 1:
        return tup[a, b, c]
    elif int(par_a) and int(par_c) and int(par_d) == 1:
        return a, c, d
    elif int(par_b) and int(par_c) and int(par_d) == 1:
        return b, c, d
    elif int(par_a) and int(par_b) == 1:
        return a, b
    elif int(par_a) and int(par_c) == 1:
        return a, c
    elif int(par_a) and int(par_d) == 1:
        return a, d
    elif int(par_b) and int(par_c) == 1:
        return b, c
    elif int(par_b) and int(par_d) == 1:
        return b, d
    elif int(par_c) and int(par_d) == 1:
        return c, d
    elif int(par_a) == 1:
        return a
    elif int(par_b) == 1:
        return b
    elif int(par_c) == 1:
        return c
    elif int(par_d) == 1:
        return d