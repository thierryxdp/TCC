def pontos_por_time(l):
    t1=l[0][0]
    t2=l[0][1]
    p01=l[0][2][0]
    p02=l[0][2][1]
    p11=l[1][2][0]
    p12=l[1][2][1]
    	
    	
        if p01>p02 and p11>p12:
            pt1 = 6
            pt2 = 0    
        elif p01<p02 and p11>p12:
            pt1 = 3
            pt2 = 3
            
   	d={t1:pt1,t2:pt2}
    return d