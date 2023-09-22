def pontos_por_time(L1,L2):
    Time1=str(L1[0])
    Time2=str(L2[0])
    if L1[2][0]>L1[2][1]:
        T1a=3 
        T2a=0
    elif L1[2][1]>L1[2][1]:
        T1a=0
        T2a=3
    else:
        T1a=1
        T2a=1
	if L2[2][0]>L2[2][1]:
        T1b=3 
        T2b=0
    elif L2[2][0]>L2[2][1]:
        T1b=0
        T2b=3
    else:
        T1b=1
        T2b=1 
        
    Total = {Time1:(T1a+T1b), Time2:(T2a+T2b)}
    return Total