def melhor_volta(x):
    """retorna o corredor com melhor volta, o tempo dessa volta e em que volta ocorreu;
    list -> tuple"""
    mtemp = 0
    ret = ('a', 1000, 'v')
    for a in range(len(x)):
        for b in range(len(x[a])):
            if x[a][b] < ret[2] :
                ret = ('x',x[a][b],'b')
    return ret