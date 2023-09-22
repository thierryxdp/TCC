"""
"""
def filtra_pares(a, b, c, d):
    par_a = a%2
    par_b = b%2
    par_c = c%2
    par_d = d%2
    if par_a == 0:
        return a
    if par_b == 0:
        return b
    if par_c == 0:
        return c
    if par_d == 0:
        return d
    if par_a and par_b == 0:
        return a, b
    if par_a and par_c == 0:
        return a, c
    if par_a and par_d == 0:
        return a, d
    if par_b and par_c == 0:
        return b, c
    if par_b and par_d == 0:
        return b, d
    if par_c and par_d == 0:
        return c, d
    if par_a and par_b and par_c == 0:
        return a, b, c
    if par_a and par_c and par_d == 0:
        return a, c, d
    if par_b and par_c and par_d == 0:
        return b, c, d
    if par_a and par_b and par_c and par_d == 0:
        return a, b, c, d