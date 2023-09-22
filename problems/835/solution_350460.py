def melhor_volta(m):
    ''' Retorna de quem foi a melhor volta, qual o tempo e em que volta'''
    l0 = [min(n) for n in m]
    l1 = [n.index(min(n) for n in m]
    i = l0.index(min(l0))
    j = l1[i]
    return i+1, min(l0), j+1