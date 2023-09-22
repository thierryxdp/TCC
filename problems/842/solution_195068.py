def pontos_por_time(lista):
    Jogodeida=lista[0]
    Jogodevolta=lista[1]
    time1=Jogodeida[0]
    time2=Jogodeida[1]
    y=Jogodeida[2]
    x=Jogodevolta[2]
    a1=y[0]
    a2=y[1]
    b2=x[0]
    b1=x[1]
    if a1>a2 and b1>b2:
        P1=6
        P2=0
    elif a1>a2 and b1==b2 or a1==a2 and b1>b2:
        P1=4
        P2=1
    elif a1==a2 and b1==b2:
        P1=2
        P2=2
    elif a1<a2 and b1>b2 or a1>a2 and b1<b2:
        P1=3
        P2=3
    elif a1==a2 and b1<b2 or a1<a2 and b1==b2:
        P1=1
        P2=4
    else:
        P1=0
        P2=6
        
    return {time1:P1,time2:P2}