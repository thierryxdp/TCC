def pontos_por_time(jogo):
    jogo1=jogo[0]
    jogo2=jogo[1]
    time1=jogo1[0]
    time2=jogo1[1]
    [x,y]=jogo1[3]
    time2=jogo2[0]
    time1=jogo2[1]
    [t,r]=jogo2[3]
   
    pontuacao= { time1: ptime1[0]+ptime2[1],time2:ptime2[0]+ptime2[1]}
    ptime1=[0,]
    ptime2=[0,]

    if x==y :
        ptime1[0]= 1
        ptime2[0]= 1
    if x>y:
        ptime1[0]=3
    if y>x:
        ptime2[0]= 3
    if t==r:
        ptime1[1]=1
        ptime2[1]= 1
    if t>r:
        ptime2[1]=3
    if r>t:
        ptime1[1]=3
    return pontuacao