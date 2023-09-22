def filtra_pares(t):
    '''filtra os números pares de uma tupla(t)'''
    tupla_par=tuple()
    if t[0] % 2==0:
        tupla_par = tupla_par+(t[0],)
    if t[1] % 2==0:
         tupla_par = tupla_par+(t[1],)
    if t[2] % 2==0:
         tupla_par = tupla_par+(t[2],)
    if t[3] % 2==0:
         tupla_par = tupla_par+(t[3],)
    return tupla_par