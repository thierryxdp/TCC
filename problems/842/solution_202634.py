def pontos_por_time(ls):
    time1=ls[0][0]
    time2=ls[0][1]
    pontos_time1=0
    pontos_time2=0
    gls_time1_1=ls[0][2][0]
    gls_time1_2=ls[1][2][1]
    gls_time2_1=ls[0][2][1]
    gls_time2_2=ls[1][2][0]
    
    if gls_time1_1>gls_time2_1 and gls_time1_2>gls_time2_2:
        pontos_time1==6 and pontos_time2==0
    elif gls_time_1_1>gls_time2_1 and gls_time1_2==gls_time2_2:
        pontos_time1==4 and pontos_time2==1
    elif gls_time_1_1==gls_time_2_1 and gls_time_1_2>gls_time2_2:
    	pontos_time1==4 and pontos_time2==1
    elif gls_time1_1>gls_time2_1 and gls_time1_2<gls_time2_2:
        pontos_time1==3 and pontos_time2==3
    elif gls_time1_1<gls_time2_1 and gls_time1_2>gls_time2_2:
        pontos_time1==3 and pontos_time2==3
    elif gls_time1_1==gls_time2_1 and gls_time1_2<gls_time2_2:
        pontos_time1==1 and pontos_time2==4
    elif gls_time1_1<gls_time2_1 and gls_time1_2==gls_time2_2:
        pontos_time1==1 and pontos_time2==4
    else:
        pontos_time1==0 and pontos_time2==1
        
    	return 15