def pontos_por_time(time1,time2):
    
    jogo1time1=lista[0][2][0]
    jogo1time2=lista[0][2][1]
    jogo2time1=lista[1][2][1]
    jogo2time2=lista[1][2][0]
    time1=lista[0][0]
    time2=lista[0][1]
    
    if jogo1time1>jogo1time2 and jogo2time1>jogo2time2:
        return {time1:6, time2:0}
    if jogo1time1>jogo1time2 and jogo2time1==jogo2time2:
        return {time1:4,:time2:0}
    if jogo1time1==jogo1time2 and jogo2time1==jogo2time2:
        return {time1:2, time2:2}
    if jogo1time1==jogo1time2 and jogo2time1<jogo2time2:
        return{time1:1, time2:4}
    if jogo1time1<jogo1time2 and jogo2time1<jogo2time2:
        return{time1: 0, time2: 6}
    if jogo1time1>jogo1time2 and jogo2time1<jogo2time2:
        return{time1:3, time2:3}
    if jogo1time1<jogo1time2 and jogo2time1>jogo2time2:
        return {time1:3, time2:3}
    if jogo1time1==jogo1time2 and jogo2time1>jogo2time2:
        return {time1: 4, time2:1}