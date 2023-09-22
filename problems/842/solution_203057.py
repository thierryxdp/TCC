def pontos_por_time(jogo):
    x=0
    y=0
    partida1=jogo[0]
    partida2=jogo[1]
    time1=partida1[0]
    time2=partida1[1]
    placar1=partida1[2]
    placar2=partida2[2]
    Agoltime1=placar1[0]
    Agoltime2=placar1[1]
    Bgoltime1=placar2[1]
    Bgoltime2=placar2[0]
    if Agoltime1>Agoltime2:
        x+=3
    elif Agoltime1<Agoltime2:
        y+=3
    else:
        x+=1
        y+=1
    if Bgoltime1>Bgoltime2:
        x+=3
    elif Bgoltime1<Bgoltime2:
        y+=3
    else:
        x+=1
        y+=1
    h={time1:x,time2:y}
    return h