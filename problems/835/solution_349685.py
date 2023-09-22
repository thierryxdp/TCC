def melhor_volta(m):
    '''
    A função retorna quem fez a melhor volta, o tempo 
    e em que volta, de uma corrida de 10 voltas com 6 
    competidores
    matriz --> tuple
    '''
    p = []
    l = []
    v = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if min(m[i]) == m[i][j]:
                p += [i + 1]
                l += [m[i][j]]
                v += [j + 1]
    return p[list.index(l, min(l))], min(l), v[list.index(l, min(l))]