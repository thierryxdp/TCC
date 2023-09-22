def filtra_pares(t):
    '''filtra os números pares de uma tupla(t)'''
    tupla_par=tuple()
    w = t[0]
    x = t[1]
    y = t[2]
    z = t[3]
    if w % 2==0:
        tupla_par = tupla_par+(w)
    if x % 2==0:
         tupla_par = tupla_par+(x)
    if y % 2==0:
         tupla_par = tupla_par+(y)
    if z % 2==0:
         tupla_par = tupla_par+(z)
    return tupla_par