#filtra_ares
def filtra_pares(t):
    """funcao que recebe uma tupla com 4 elementos inteiros e retorna os elementos pares na mesma ordem original,
       tupla --> tupla"""
    x,y,w,z=t
    s = ()
    if x%2==0:
        s=s+(x,)
    if y%2==0:
        s=s+(y,)
    if w%2==0:
        s=s+(w,)
    if z%2==0:
        s=s+(z,)