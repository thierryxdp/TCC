#Start your python function here
def pontos(p):
    t1=ls[0]
    t2=ls[1]
    g1=ls[2][0]
    g2=ls[2][1]
    if gi<g2:
        return (t1,0,t2,3)
    if g1==g2:
        return(t1,1,t2,3)
    else:
        return (t1,3,t2,0)
    
def contab (d,ps):
    t1=ps[0]
    p1=ps[1]
    t2=ps[2]
    p2=ps[3]
    d[t1]+=p1 
    f[t2]+=p2
    
def name1(p):
    return p[0]

def pontos_por_times(ls):
    d={name1(ls[0]):0, name1(ls[1]):0}
    ps=pontos(ls[0])
    contab(d,ps)
    ps=pontos(ls[1])
    contab(d,ps)
    return d