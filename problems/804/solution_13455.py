def filtra_pares (a,b,c,d):
    '''Filtra as variaveis a,b,c e d se forem pares serão retornadas, 
    caso não sejam, não seram retornadas'''
    t=(a,b,c,d)
    t2=()
    if a%2==0:
        t2.append(t(0))
        if b%2==0:
            t2.append(t(1))
            if c%2==0:
                t2.append(t(2))
                if d%2==0:
                    t2.append(t(3))
                    return t2