def pontos_por_time(l):
    ti1=(l[0])[0]
    ti2=(l[0])[1]
    pi1=((l[0])[2])[0]    
    pi2=((l[0])[2])[1]     
    tv1=(l[1])[0]
    tv2=(l[1])[1]
    pv1=((l[1])[2])[0]    
    pv2=((l[1])[2])[1]             
    if pi1>pi2 and pv1>pv2:
   		pt1= pi1*3 + pi2*3
        	return d={ti1:pt1,ti2:0}
        else:
            return 0