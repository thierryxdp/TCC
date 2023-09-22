def pontos_por_time(jogo):
    time1=''
    time2=''
    k=[x,y]
    c=[t,r]
    x,y,r,t=int
    jogo=[[time1,time2,k],[time2,time1,c]]
    pontuacao = { time1: ptime1[0]+ptime2[1],time2:ptime2[0]+ptime2[1]}
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