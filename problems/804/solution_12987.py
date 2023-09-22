def filtra_pares(f):
    tupla = ()
    if f[0] % 2 == 0:
        tupla = tupla + (f[0],)
    if f[1] % 2 == 0:
        tupla = tupla + (f[1],)
    if f[2] % 2 == 0:
        tupla = tupla + (f[2],)
    if f[3] % 2 == 0:
        tupla = tupla + (f[3],)
    return tupla#Start your python function here