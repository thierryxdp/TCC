def filtra_pares(t):
    '''Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original'''
    x,y,w,z=t
    s=()
    if x%2==0:
        s=s+(x,)
    if y%2==0:
        s=s+(y,)
    if w%2==0:
        s=s+(w,)
    if z%2==0:
        s=s+(z,)
    return s#Start your python function here