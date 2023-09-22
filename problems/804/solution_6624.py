def filtra_pares(t):
    ''' funcao que recebe uma tupla e retorna uma nova tupla contendo apenas pares originais, na mesma ordem em que se encontravam.
    tupla->tupla '''
    x,y,w,z = t
    s= ()
    if (x%2==0):
        s=s+(x,)
    if (y%2==0):
        s=s+(y,)
    if (w%2==0):
        s=s+(w,)
    if (z%2==0):
        s=s+(z,)
        return s;