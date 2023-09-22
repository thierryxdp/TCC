def melhor_volta(m):
    ''' Essa função retorna quem fez a melhor volta dentre os corredores
    de uma corrida;
    list -> tuple. '''
    t = m[0][0]
    a = len(m)
    w = 0
    for i in range(a):
        t_runner = min(m[i])
        if t_runner < t:
            t = t_runner
            w = i
    v = list.index(m[w], t)
    return w + 1, t, v + 1