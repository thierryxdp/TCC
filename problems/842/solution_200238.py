def pontos_por_time(lista=[]):
    '''função que retorna o resultado de um campeonato dados os numeros de gols feitos por cada time
    list->dic'''
    jogo_ida=lista[0]
    jogo_volta=lista[1]
    time1=jogo_ida[0]
    time2=jogo_ida[1]
    placar_ida=jogo_ida[2]
    placar_volta=jogo_volta[2]
    if placar_ida[0]>placar_ida[1] and placar_volta[0]>placar_volta[1] :
        return {time1: 6, time2: 0}
    elif placar_ida[0]< placar_ida[1] and placar_volta[0]< placar_volta[1]:
        return {time1: 0, time2: 6}
    elif placar_ida[0]<placar_ida[1] and placar_volta[0]>placar_volta[1]:
        return {time1:3, time2:3}
    elif placar_ida[0]<placar_ida[1] and placar_volta[0]== placar_volta[1]:
        return { time1:4, time2: 1}
    elif placar_ida[0]==placar_ida[1] and placar_volta[0]< placar_volta[1]:
        return { time1: 2, time2: 2}