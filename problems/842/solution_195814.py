def pontos_por_time(jogo):
    time1=jogo[0]
    time2=jogo[1]
    placar1=jogo[2]
    time3=jogo[0]
    time4=jogo[1]
    placar2=jogo[2]
    x=placar1[0]
    y=placar1[1]
    t=placar2[0]
    r=placar2[1]
   
    pontuacao{ time1: ptime1[0]+ptime2[1],time2:ptime2[0]+ptime2[1]}
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