def ponto_por_time(x):
    d={}
    time1=x[0][0]
    time2=x[0][1]
    gol1=x[0][2][0]
    gol2=x[0][2][1]
    gol3=x[1][2][0]
    gol4=x[1][2][1]
    if gol1>gol2:
        P1=3
        P2=0
    elif gol1<gol2:
        P1=0
        P2=3
    else: 
        P1=1
        P2=1