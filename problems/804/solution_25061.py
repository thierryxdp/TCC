def filta_pares(tup):
    '''Retorna uma tupla contendo os elementos pares da tupla t de
    4 elementos; (int, int, int, int) -> (int, int, int, int)'''
    if tup[0]/2==tup[0]//2:
        a=(tup[0],)
    else:
        a=()
    if tup[1]/2==tup[1]//2:
        b=(tup[1],)
    else:
        b=()
    if tup[2]/2==tup[2]//2:
        c=(tup[2],)
    else:
        c=()
    if tup[3]/2==tup[3]//2:
        d=(tup[3],)
    else:
        d=()
    return a+b+c+d