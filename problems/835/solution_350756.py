def melhor_volta(m):
    """ Dada a matriz m 6x10 com 10 tempos de 6 corredores em uma pista de Kart,
    retorna uma tupla com quem fez a melhor volta, com qual tempo e em que volta.
    list -> tuple"""
    t = []
    l = [0,0,0]
    for a in m:
        for b in a:
            t.append(b)
    return t