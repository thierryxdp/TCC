def pontos_por_time(x):
    d={}
    time1=x[0][0]
    time2=x[0][1]
    if x[0][2][0]>x[0][2][1]:
        p1=3
        p2=0
    elif x[0][2][0]<x[0][2][1]:
        p2=3
        p1=0
    else:
        p1=1
        p2=1
    if x[1][2][0]>x[1][2][1]:
        p2+=3
        p1+=0
    elif x[1][2][1]>x[1][2][0]:
        p1+=3
    else:
        p1+=1
        p2+=1
    return d