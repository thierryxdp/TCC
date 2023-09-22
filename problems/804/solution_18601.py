"""
"""
def filtra_pares(a, b, c, d):
    par_a = a%2
    par_b = b%2
    par_c = c%2
    par_d = d%2
    if par_a and par_b and par_c and par_d == 0:
        return a, b, c, d
    elif par_a == 0:
        return a
    elif par_b == 0:
        return b
    elif par_c == 0:
        return c
    elif par_d == 0:
        return d
    elif par_a and par_b == 0:
        return a, b
    elif par_a and par_c == 0:
        return a, c
    elif par_a and par_d == 0:
        return a, d
    elif par_b and par_c == 0:
        return b, c
    elif par_b and par_d == 0:
        return b, d
    elif par_c and par_d == 0:
        return c, d
    elif par_a and par_b and par_c == 0:
        return a, b, c
    elif par_a and par_c and par_d == 0:
        return a, c, d
    elif par_b and par_c and par_d == 0:
        return b, c, d
    else:
        return 'Nenhum valor esperado'