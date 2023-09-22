def pontos_por_time(jogo):
    ''
    time1 = jogo[0][0] 
    time2 = jogo[1][0] 
    if jogo[0][2][0]>jogo[0][2][1] and jogo[1][2][1]>jogo[1][2][0]:
        return {time1:6, time2:0}
    if jogo[0][2][0]<jogo[0][2][1] and jogo[1][2][1]<jogo[1][2][0]:
        return {time1:0, time2:6}
    if jogo[0][2][0]>jogo[0][2][1] and jogo[1][2][1]=jogo[1][2][0]:
        return {time1:4, time2:1}
    if jogo[0][2][0]<jogo[0][2][1] and jogo[1][2][1]=jogo[1][2][0]:
        return {time1:1, time2:4}