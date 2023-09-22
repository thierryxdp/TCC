def pontos_por_time(lista):
    '''
    '''
    jogo1=lista[0]
    jogo2=lista[1]
    result1=jogo1[2]
    result2=jogo2[2]
    time1=jogo1[0]
    time2=jogo1[1]
    
    if result1[0]>result1[1] and result2[0]<result1[1]:
        return {time2:6,
                time1:0}
    elif result1[0]<result1[1] and result2[0]>result1[1]:
        return {time1:0,
                time2:6}
    elif result1[0]==result1[1] and result2[0]==result1[1]:
        return {time1:2,
                time2:2}
    elif result1[0]>result1[1] and result2[0]==result1[1]:
        return {time1:4,
                time2:1}
    elif result1[0]<result1[1] and result2[0]==result1[1]:
        return {time1:1,
                time2:4}
    elif result1[0]==result1[1] and result2[0]<result1[1]:
        return {time1:4,
                time2:1}
    elif result1[0]==result1[1] and result2[0]>result1[1]:
        return {time1:1,
                time2:4}#Start your python function here