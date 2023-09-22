def pontos_por_time(l2):
    time1=l2[0][0]
    time2=l2[1][0]
    if l2[0][2][0]>l2[0][2][1]:
        p1=3
        p2=0
    elif l2[0][2][0]==l2[0][2][1]:
        p1=1
        p2=1
    else:
        p1=0
        p2=3
    
    if l2[1][2][1]>l2[0][2][0]:
        p1=3+p1
        p2=0+p2
    elif l2[0][2][1]==l2[0][2][0]:
        p1=1+p1
        p2=1+p2
    else:
        p1=0+p1
        p2=3+p2
    d={time1:p1,time2:p2}