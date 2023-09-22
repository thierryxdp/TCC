def filtra_pares (a,b,c,d):
    '''Filtra as variaveis a,b,c e d se forem pares serão retornadas, 
    caso não sejam, não seram retornadas'''
    t=(a,b,c,d)
    t2=()
    if t[0]%2==0:
        t2.append(t[0])
    if t[1]%2==0:
        t2.append(t[1])
    if t[2]%2==0:
        t2.append(t[2])
    if t[3]%2==0:
        t2.append(t[3])
    return t2