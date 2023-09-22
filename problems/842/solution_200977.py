def pontos_por_time(lista):
    '''
    '''
    jogo1=lista[0]
    jogo2=lista[1]
    result1=jogo1[1]
    result2=jogo2[1]
    
    if result1[0]>result1[1] and result2[0]<result1[2]:
        return {jogo1[1]:6,
                jogo1[2]:0}
    elif result1[0]<result1[1] and result2[0]>result1[2]:
        return {jogo1[1]:0,
                jogo1[2]:6}
    elif result1[0]==result1[1] and result2[0]==result1[2]:
        return {jogo1[1]:2,
                jogo1[2]:2}
    elif result1[0]>result1[1] and result2[0]==result1[2]:
        return {jogo1[1]:4,
                jogo1[2]:1}
    elif result1[0]<result1[1] and result2[0]==result1[2]:
        return {jogo1[1]:1,
                jogo1[2]:4}
    elif result1[0]==result1[1] and result2[0]<result1[2]:
        return {jogo1[1]:4,
                jogo1[2]:1}
    elif result1[0]==result1[1] and result2[0]>result1[2]:
        return {jogo1[1]:1,
                jogo1[2]:4}