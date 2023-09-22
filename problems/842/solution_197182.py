def pontos_por_time(x,y):
    Time1=str(x[0])
    Time2=str(y[0])
    if x[2][0]>x[2][1]:
        T1a=3 
        T2a=0
    elif x[2][0]<x[2][1]:
        T1a=0
        T2a=3
    else:
        T1a=1
        T2a=1
    if y[2][0]>y[2][1]:
        T1b=3 
        T2b=0
    elif y[2][0]<y[2][1]:
        T1b=0
        T2b=3
    else:
        T1b=1
        T2b=1 
        
    Total = {Time1:(T1a+T1b), Time2:(T2a+T2b)}
    return Total