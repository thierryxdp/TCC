def ptime(l):
    t1=str(l[0][0])
    t2=str(l[1][0])
    a=(l[0][2][0])
    b=(l[0][2][1])
    c=(l[1][2][0])
    d=(l[1][2][1])
    p1=[a,b]
    p2=[c d]
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
        b=placar1+1
    if c>d:
        c=placar2+3
        d=placar2
    elif c<d:
        d=placar2+3
        c=placar2
    else: 
        c=placar1+1
        d=placar1+1
    total_pontos1=a+b
    total_pontos2=c+b
    return {t1:total_pontos1,t2:total_pontos2}