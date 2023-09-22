def filtra_pares(t):
    """ função que receba uma tupla com 4 elementos inteiros e retorne uma nova tupla contendo apenas os elementos pares"""
    x,y,w,z=t
    s= ()
    if x%2==0:
        s=s+(x,)
    if y%2==0:
        s=s+(y,)
    if w%2==0:
        s=s+(w,)
    if z%2==0:
        s=s+(z,)
    return s