def pontos_por_time(ls):
    d={name1(ls[0]):0,name1(ls[1]):0}
    ps=pontos(ls[0])
    contab(d,ps)
    ps=pontos(ls[1])
    contab(d,ps)
    return d

def pontos(ls):
    t1=ls[0]
    t2=ls[1]
    gs=ls[2]
    if gs[0]<gs[1]:
        return (t1,0,t2,3)
    if gs[0]==gs[1]:
        return (t1,1,t2,1)
    return (t1,3,t2,0)

def contab(d,ps):
    t1=ps[0]
    t2=ps[2]
    p1=ps[1]
    p2=ps[3]
    d[t1]+=p1
    d[t2]+=p2
    
def name1(ls):
    return ls[0]