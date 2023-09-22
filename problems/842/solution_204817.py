def pontos_por_time(lista):
    time1=str(lista[0][0])
    time2=str(lista[1][0])
    a=(lista[0][2][0])
    b=(lista[0][2][1])
    c=(lista[1][2][0])
    d=(lista[1][2][1])
    pts1=[a,b]
    pts2=[c,d]
    plc1=0
    plc2=0
    if a>b:
        a=plc1+3
        b=plc1
    elif a<b:
        b=plc2+3
        a=plc2
    else:
        a=plc1+1
        b=plc2+1
    if c>d:
        c=plc1+3
        d=plc1
    elif c<d:
        d=plc2+3
        c=plc2
    else:
        c=plc1+1
        d=plc2+1
    total_pts1=a+d
    total_pts2=c+b
    return{time1:total_pts1,time2:total_pts2}