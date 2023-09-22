def filtra_pares (a,b,c,d):
    '''Filtra as variaveis a,b,c e d se forem pares serão retornadas, 
    caso não sejam, não seram retornadas'''
    t2=()
    if a%2==0:
        t2.append(a)
    if b%2==0:
        t2.append(b)
    if c%2==0:
        t2.append(c)
    if d%2==0:
        t2.append(d)
    return t2