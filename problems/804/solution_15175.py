def filtra_pares(tupla):
    tupla_par = (,)
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    if a%2 == 0:
        tupla_par = tupla_par + a,
    if b%2 == 0:
        tupla_par = tupla_par + b,
    if c%2 == 0:
        tupla_par = tupla_par + c,
    if d%2 == 0:
        tupla_par = tupla_par + d,
    return tupla_par