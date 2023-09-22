def melhor_volta(m):
    """ Dada a matriz m 6x10 com 10 tempos de 6 corredores em uma pista de Kart,
    retorna uma tupla com quem fez a melhor volta, com qual tempo e em que volta.
    list -> tuple"""
    t = []
    l = [0,0,0]
    for a in m:
        for b in a:
            t.append(b)
    for a in range(len(m)):
        for b in range(len(m[0])):
            if min(t) == m[a][b]:
                l[0] = a
                l[1] = min(t)
                l[2] = b
    return (l[0],l[1],l[2])