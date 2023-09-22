def filtra_pares(tupla):
    tupla_par = ()
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    for n in tupla:
        if n%2 == 0:
            tupla_par = tupla_par + n,
    return tupla_par