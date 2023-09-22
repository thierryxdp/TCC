def pt(ls):
    d={name1(ls[0]):0, name1(ls[1]):0}
    p1=pontos(ls[0])
    contab(d,p1)
    p2=pontos(ls[1])#
    contab(d,p2)
    return d
       
    def pontos(ls):
       t1=ls[0]
       t2=ls[1]
       g1=ls[2][0]
       g2=ls[2][1]
       if g1<g2:
       	return(t1,3,t2,0)
       if g2<g1:
       	return(t1,0,t2,3)
       return(t1,1,t2,3)
    def cont(d,t):
       t1=t[0]
       t2=t[2]
       d[t1]=d[t1]+t{1]
       d[t2]=d[t1]+t{3}
    def name1(ls):
    	return ls[0]