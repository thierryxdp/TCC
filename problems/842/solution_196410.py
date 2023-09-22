def pontos_por_time (jogos):
    [jogo1,jogo2] = jogos
    [time1,time2,[gols1j1,gols2j1]] = jogo1
    [time2,time1,[gols2j2,gols1j2]] = jogo2
    #jogo1 = [time1,time2,[gols1j1,gols2j1]]
    #jogo2 = [time2,time1,[gols2j2,gols1j2]]
     

    if gols1j1 > gols2j1:
        ptsTime1j1 = 3
        ptsTime2j1 = 0
    if gols1j1 < gols2j1:
        ptsTime1j1 = 0
        ptsTime2j1 = 3
    if gols1j1 == gols2j1:
        ptsTime1j1 = 1
        ptsTime2j1 = 1
        
    if gols1j2 > gols2j2:
        ptsTime1j2 = 3
        ptsTime2j2 = 0
    if gols1j2 < gols2j2:
        ptsTime1j2 = 0
        ptsTime2j2 = 3
    if gols1j2 == gols2j2:
        ptsTime1j2 = 1
        ptsTime2j2 = 1    

    ptsTotal1 = ptsTime1j1 + ptsTime1j2
    ptsTotal2 = ptsTime2j1 + ptsTime2j2
    
    if ptsTotal1 > ptsTotal2:
        return {time1:ptsTotal1, time2:ptsTotal2}
    if ptsTotal2 > ptsTotal1:
        return {time2:ptsTotal2, time1:ptsTotal1}
    if ptsTotal1 == ptsTotal2:
        return {time1:ptsTotal1, time2:ptsTotal2}