def pontos_por_time(ls):
    t1 = {ls[0][1]: 6, ls[0][0]:0}
    t2 = {ls[0][1]: 0, ls[0][0]:6}
    t3 = {ls[0][1]: 2, ls[0][0]:2}
    t4 = {ls[0][1]: 3, ls[0][0]:3}
    t5 = {ls[0][1]: 4, ls[0][0]:1}
    t6 = {ls[0][1]: 1, ls[0][0]:4}
    return t1
             
    
    def contato(d,t):
        t1 = t[0]
        t2 = t[2]
        d[t1] = d[t1]+t[1]
        d[t2] = d[t2]+t[3]
        def nome1(ls):
        	return ls[0]