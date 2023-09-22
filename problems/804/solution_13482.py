def filtra_pares (a):
    '''Filtra as variaveis a,b,c e d se forem pares serão retornadas, 
    caso não sejam, não seram retornadas'''
    t=(a)
    t2=()
    if t[0]%2==0:
        t2=t2 + (t[0],)
    if t[1]%2==0:
        t2=t2 + (t[1],)
    if t[2]%2==0:
        t2=t2 + (t[2],)
    if t[3]%2==0:
        t2=t2 + (t[3],)
    return t2