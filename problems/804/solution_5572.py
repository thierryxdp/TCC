def filtra_pares(a, b, c, d):
    a_par = a%2 == 0
    b_par = b%2 == 0
    c_par = c%2 == 0
    d_par = d%2 == 0
    if a_par and b_par and c_par and d_par:
        return (a, b, c, d)
    elif a_par and b_par and c_par:
        return (a, b, c)
    elif a_par and b_par and d_par:
        return (a, b, d)
    elif a_par and c_par and d_par:
        return (a, c, d)
    elif b_par and c_par and d_par:
        return (b, c, d)
    elif a_par and b_par:
        return (a, b)
    elif a_par and c_par:
        return (a, c)
    elif a_par and d_par:
        return (a, d)
    elif b_par and c_par:
        return (b, c)
    elif b_par and d_par:
        return (b, d)
    elif c_par and d_par:
        return (c, d)
    elif a_par:
        return (a)
    elif b_par:
        return (b)
    elif c_par:
        return (c)
    elif d_par:
        return (d)
    else:
        return 'não tem número par'