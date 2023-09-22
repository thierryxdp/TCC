def pontos_por_time(lista=[]):
    '''blablabla'''
    jogo_ida=lista[0]
    jogo_volta=lista[1]
    time1=jogo_ida[0]
    time2=jogo_ida[1]
    placar_ida=jogo_ida[2]
    placar_volta=jogo_volta[2]
    if (placar_ida[0])>(placar_ida[1]) and (placar_volta[1])>(placar_volta[0]):
        return {jogo_ida[0]: 6, jogo_ida[1]: 0}
    elif (placar_ida[0])<(placar_ida[1]) and (placar_volta[1])<(placar_volta[0]):
        return {jogo_ida[0]: 0, jogo_ida[1]: 6}
    elif (placar_ida[0])<(placar_ida[1]) and (placar_volta[1])>(placar_volta[0]):
        return {jogo_ida[0]: 3, jogo_ida[1]: 3}
    elif (placar_ida[0])>(placar_ida[1]) and (placar_volta[1])<(placar_volta[0]):
        return {jogo_ida[0]: 3, jogo_ida[1]: 3}
    elif (placar_ida[0])==(placar_ida[1]) and (placar_volta[1])==(placar_volta[0]):
        return {jogo_ida[0]: 2, jogo_ida[1]: 2}
    elif (placar_ida[0])<(placar_ida[1]) and (placar_volta[1])==(placar_volta[0]):
        return {jogo_ida[0]: 1, jogo_ida[1]: 4}