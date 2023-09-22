def pontos_por_time(L):
    time1=0
    time2=0
      
    if jogo[0][2][0]>jogo[0][2][1]:
        time1=time1+3
    elif jogo[0][2][0]>jogo[0][2][1]:
        time2=time2+3
    else:
        time1=time1+1
        time2+time2+1
    if jogo[1][2][0]>jogo[1][2][1]:
        time1=time1+3
    elif jogo[1][2][0]<jogo[1][2][1]:
        time2=time2+3
    else:
        time1=time1+1
        time2=time2+1
    return{'nomet1','nomet2':[time1,time2], 'nomet2','nomet1':[time2,time1]}