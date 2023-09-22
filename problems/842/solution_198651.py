def pontos_por_time(l2):
    time1=l2[0][0]
    time2=l2[1][0]
    
    g11=l2[0][2][0]
    g21=l2[0][2][1]
    
    g12=l2[1][2][0]
    g22=l2[0][2][1]
    
    if g11>g21:
        p1=3
        p2=0
    elif g11<g21:
        p1=
        p2=3
    else:
        p1=1
        p2=1
    
    if g12>g22:
        p1=3+p1
        p2=0+p1
    elif g12<g22:
        p1=0+p1
        p2=3+p2
    else:
        p1=1+p1
        p2=2+p2
    
    d={time1:p1,time2:p2}