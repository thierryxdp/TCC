#filtra_ares
def filtra_pares(t):
    """funcao que recebe uma tupla com 4 elementos inteiros e retorna os elementos pares na mesma ordem original,
       tupla --> tupla"""
    if x%2==0:
        s=s+(x,)
    elif y%2==0:
        s=s+(y,)
    elif w%2==0:
        s=s+(w,)
    else:
        s=s+(z,)
    x,y,z,w=t
    s = ()