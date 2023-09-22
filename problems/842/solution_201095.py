def pontos_por_time(l):
    ti1=(l[0])[0]
    ti2=(l[0])[1]
    pi1=((l[0])[2])[0]    
    pi2=((l[0])[2])[1]     
    tv1=(l[1])[0]
    tv2=(l[1])[1]
    pv1=((l[1])[2])[0]    
    pv2=((l[1])[2])[1]             
    if pv1>pv2 and pi1>pi2:
        return pt1 = pv1*3 + pi1*3 and pt2=0
    elif pv1>pv2 and pi1<pi2:
    	return pt1 = pv1*3 and pt2 = pi2*3
    elif pv1<pv2 and pi1<pi2:
    	return pt2 = pi2*3 + pv2*3 and pt1=0
    elif pv1<pv2 and pi1>pi2:
        return pt1 = pi1*3 and pt2= pv2*3
    elif pv1 = pv2 and pi1>pi2:
        return pt1 = pi1*3 + pv1 and pt2 = pv2
    elif pv1 = pv2 and pi1<pi2:
        return pt1 = pv1 and pt2 = pi2*3 + pv2
    elif pv1 < pv2 and pi1 = pi2:
        return pt1= pi1 and pt2 = pv2*3 + pi2
    elif pv1 > pv2 and pi1=pi2:
        return pt1=pv1*3 + pi1 and pt2 = pi2
    else:
        return pt1 = pi1 + pv1 and pt2 = pi2 + pv2
ti1=tv2
ti2=tv1
	return d{ti1:pt1,ti1:pt2}