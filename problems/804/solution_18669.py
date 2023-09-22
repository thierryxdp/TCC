def filtra_pares(tupple):
    tupple = a, b, c, d
    par_a = a%2==0
    par_b = b%2==0
    par_c = c%2==0
    par_d = d%2==0
    if int(par_a) and int(par_b) and int(par_c) and int(par_d) == 1:
        return str('a, b, c, d')
    elif int(par_a) and int(par_b) and int(par_c) == 1:
        return a, b, c
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