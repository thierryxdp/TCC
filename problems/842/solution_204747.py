def pontos_por_time(lista):
    time1=str(lista[0][0])
    time2=str(lista[1][0])
    a=(lista[0][2][0])
    b=(lista[0][2][1])
    c=(lista[1][2][0])
    d=(lista[1][2][1])
    pontos1=[a,b]
    pontos2=[c,d]
    placar1=0
    placar2=0
    if a>b:
        a=placar1+3
        b=placar1
    elif a<b:
        b=placar2+3
        a=placar2
    else:
        a=placar1+1
        b=placar2+1
    if c>d:
        c=placar1+3
        d=placar1
    elif c<d: 
        d=placar2+3
        c=placar2
    else:
        c=placar1+1
        d=placar2+1
    total_pontos1=a+d
    total_pontos2=c+b
    return {time1:total_pontos1,time2:total_pontos2}