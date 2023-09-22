def pontos_por_time(ida,volta):
    time1:ida[0]
    time2:ida[1]
    placar1:ida[2]
    gol1=placar1[0]
    gol2=placar1[1]
    time2:volta[0]
    time1:volta[1]
    placar2:volta[2]
    gol4=placar2[0]
    gol3=placar2[1]
    
    if (gol1==gol2) and (gol3==gol4):
        return {time1:1,time2:1}
    elif (gol1>gol2) and (gol3>gol4):
        return {time1:6,time2:0}
    elif (gol1<gol2) and (gol3<gol4):
        return {time1:0,time2:6}
    elif (gol1<gol2) and (gol3>gol4):
        return {time1:3,time2:3}