def pontos_por_time(x):
    time1=x[0][0]
    time2=x[0][1]
    pontos1= 3*v+e
    pontos2= 3*V+E
    if x[0][2][0]>x[0][2][1]:
        v=3 and V=0
    if x[0][2][0]==x[0][2][1]:
        e==E=1
    if x[1][2][0]<x[1][2][1]:
        V=3 and v=0
    if x[1][2][0]==x[1][2][1]:
        e==E=1 
    dic={time1:pontos1 ,time2:pontos2 }
    return dic