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
    return{jogoi[0]:[time1, time2] , jogov[1]: [time2,time1]}