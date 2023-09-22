def pontos_por_time(jogos):
    time1=(jogos[0])[0]
    time2=(jogos[0])[1]
    gol1ida=((jogos[0])[2])[0]
    gol2ida=((jogos[0])[2])[1]
    gol2volta=((jogos[1])[2])[0]
    gol1volta=((jogos[1])[2])[1]
    if (gol1ida-gol2ida)>0:
        r1ida=3 
        r2ida=0
    if (gol1ida-gol2ida)<0:
        r1ida=0 
        r2ida=3
    if gol1ida==gol2ida:
        r1ida=1
        r2ida=1
    if (gol1volta-gol2volta)>0:
        r1volta=3 
        r2volta=0
    if (gol1volta-gol2volta)<0:
        r1volta=0 
        r2volta=3
    if gol1volta==gol2volta:
        r1volta=1
        r2volta=1    
    r1=r1ida+r1volta
    r2=r2ida+r2volta
    resultado_fase={time1:r1,time2:r2}
    return resultado_fase