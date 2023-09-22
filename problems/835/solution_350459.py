def melhor_volta(m):
    ''' Retorna de quem foi a melhor volta, qual o tempo e em que volta'''
    l0 = [min(n) for n in m]
    i = l0.index(min(l0))
    return i, min(l0)