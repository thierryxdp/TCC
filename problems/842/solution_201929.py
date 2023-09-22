#Start your python function here
def pontos_por_time(ls):
    t1 = ls[0]
    t2 = ls[1]
    g1 = ls[2][0]
    g2 = ls[2][1]
    if g1<g2:
        return (t1, 0, t2, 3)
    elif g1>g2:
        return (t1, 3, t2, 0)
    else:
   		return(t1, 1, t2, 1)
    
    def contato(d,t):
        t1 = t[0]
        t2 = t[2]
        d[t1] = d[t1]+t[1]
        d[t2] = d[t2]+t[3]
        def nome1(ls):
        	return ls[0]