def pontos_por_time(ida,volta):
    time1:ida[0]
    time2:ida[1]
    placar1:ida[2]
    gol1=placar1[0]
    gol2=placar1[1]
    time1:volta[0]
    time2:volta[1]
    placar2:volta[2]
    gol3=placar2[0]
    gol4=placar2[1]
    
    if (gol1==gol2) and (gol3==gol4):
        return {time1,time2}