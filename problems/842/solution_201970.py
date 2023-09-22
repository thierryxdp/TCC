#Start your python function here
def pontos_por_time(ls):
    if ls[0][1][0] > ls[0][1][1]:
        g1 = 3
        g2 = 0
    elif ls[0][1][0] < ls[0][1][1]:
        g1 = 0
        g2 = 3
    elif ls[0][1][0] = ls[0][1][1]:
        g1 = 1
     	g2 = 1
    if ls[1][1][0] > ls[1][1][1]:
        g3 = 3
        g4 = 0
   	elif ls[1][1][0] < ls[1][1][1]:
        g3 = 0
       	g4 = 3
    elif ls[1][1][0] = ls[1][1][1]:
        g3 = 1
        g4 = 1
 		t1 = {ls[0][0]: g1+g3, ls[0][1]:g2+g4}
     
    	return t1
    
    def contato(d,t):
        t1 = t[0]
        t2 = t[2]
        d[t1] = d[t1]+t[1]
        d[t2] = d[t2]+t[3]
        def nome1(ls):
        	return ls[0]