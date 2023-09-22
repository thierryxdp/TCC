def pontos_por_time(lista):
    '''
    '''
    jogo1 = lista[0]
    jogo2 = lista[1]
    result1 = jogo1[2]
    result2 = jogo2[2]
    if str(jogo1[0]) != str(jogo2[0]):
        if result1[0] > result1[1] and result2[0] < result2[1]:
            return {jogo1[0] : 6, jogo1[1] : 0}
        elif result1[0] < result1[1] and result2[0] == result2[1]:
            return {jogo1[0] : 1, jogo1[1] : 4}
        elif result1[0] < result1[1] and result2[0] < result2[1]:
            return {jogo1[0] : 3, jogo1[1] : 3}
        elif result1[0] > result1[1] and result2[0] > result2[1]:
            return {jogo1[0] : 3, jogo1[1] : 3}
        elif result1[0] > result1[1] and result2[0] == result2[1]:
            return {jogo1[0] : 4, jogo1[1] : 1}
        elif result1[0] == result1[1] and result2[0] == result2[1]:
            return {jogo1[0] : 2, jogo1[1] : 2}
        elif result1[0] < result1[1] and result2[0] > result2[1]:
            return {jogo1[1] : 6, jogo1[0] : 0}
        elif result1[0] == result1[1] and result2[0] > result2[1]:
            return {jogo1[0] : 1, jogo1[1] : 4}
        elif result1[0] == result1[1] and result2[0] < result2[1]:
            return {jogo1[0] : 4, jogo1[1] : 1}
    elif str(jogo1[0]) == str(jogo2[0]):
        if result1[0] > result1[1] and result2[0] < result2[1]:
            return {jogo1[0] : 3, jogo1[1] : 3}
        elif result1[0] == result1[1] and result2[0] > result2[1]:
            return {jogo1[0] : 4, jogo1[1] : 1}
        elif result1[0] == result1[1] and result2[0] == result2[1]:
            return {jogo1[0] : 2, jogo1[1] : 2}
        elif result1[0] > result1[1] and result2[0] == result2[1]:
            return {jogo1[0] : 4, jogo1[1] : 1}
        elif result1[0] == result1[1] and result2[0] < result2[1]:
            return {jogo1[0] : 1, jogo1[1] : 4}
        elif result1[0] < result1[1] and result2[0] > result2[1]:
            return {jogo1[0] : 3, jogo1[1] : 3}
        elif result1[0] > result1[1] and result2[0] > result2[1]:
            return {jogo1[0] : 6, jogo1[1] : 0}
        elif result1[0] < result1[1] and result2[0] == result2[1]:
            return {jogo1[0] : 1, jogo1[1] : 4}
        elif result1[0] < result1[1] and result2[0] < result2[1]:
            return {jogo1[0] : 0, jogo1[1] : 6}