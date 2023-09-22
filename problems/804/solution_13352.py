def filtra_pares(t):
    '''função que recebe uma tupla com 4 números inteiros e retorna uma nova tuoka apenas com os elementos pares
    tuple -> tuple'''
    p = ()
    if t[0]%2 == 0:
       p = (t[0],)
    if t[1]%2 == 0:
       p = p + (t[1],)
    if t[2]%2 == 0:
       p = p + (t[2],)
    if t[3]%2 == 0:
       p = p + (t[3],)
    
    return p