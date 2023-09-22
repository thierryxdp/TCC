def melhor_volta(m):
    ''' Retorna de quem foi a melhor volta, qual o tempo e em que volta'''
    l0 = [m.index(min(n)) for n in m]
    l1 = [min(n) for n in m]
    i = l1.index(min(l1))
    j = l0[i]
    return i, min(l1), j