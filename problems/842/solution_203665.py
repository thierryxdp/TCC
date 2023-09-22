def pt(l):
    def pontos(l):
        t1=l[0]
        t2=l[1]
        g1=l[2][0]
        g2=l[2][1]

        if g1<g2:
            return(t1,0,t2,3)
        elif g2<g1:
            return(t1,3,t2,0)
        else:
            return(t1,1,t2,1)

        def contab(d,t):
        t1=t[0]
        t2=t[2]
        d[t1]+=t[1]
        d[t2]+=t[3]

 def nome1(l):
    return l[0]

    d={nome1(l[0]):0,nome1(l[1]):0}
    p1=pontos(l[0])
    contab(d,p1)
    p2=pontos(l[1])
    contab(d,p2)
    return d

#Start your python function here