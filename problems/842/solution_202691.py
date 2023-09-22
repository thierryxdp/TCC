def pontos_por_time(ls):
    d = {name1(ls[0]): 0, name1(ls[1]):0}
    p1 = pontos(ls[0])
    contab(d,p1)
    p2= pontos(ls[1])
    contab(d,p2)
    return d
def ponto(ls):
    t1 = ls[0]
    t2 = ls[1]
    g1 = ls[2]
    g2 = ls[3]
    if g1 < g2:
        return (t1,0,t2,3)
    if g2 < g1:
        return (t1,3,t2,0)
    else:
        return (t1,1,t2,1)
def name1(g):
    return g[0]
def contab(d,p):
    d[p[0]]
    d[p[0]] += p[3]