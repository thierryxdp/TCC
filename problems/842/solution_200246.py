def pontos_por_time(lista=[]):
    '''função que retorna o resultado de um campeonato dados os numeros de gols feitos por cada time
    list->dic'''
    jogo_ida=lista[0]
    jogo_volta=lista[1]
    time1=jogo_ida[0] and jogo_volta[1]
    time2=jogo_ida[1] and jogo_volta[0]
    placar_ida=jogo_ida[2]
    placar_volta=jogo_volta[2]
    if jogo_ida[0]>jogo_ida[1] and jogo_volta[1]>jogo_volta[0]:
        return {time1:6, time2:0}
    if jogo_ida[0]<jogo_ida[1] and jogo_volta[1]<jogo_volta[0]:
        return {time1:0, time2:6}
    if jogo_ida[0]>jogo_ida[1] and jogo_volta[1]<jogo_volta[0]:
        return {time1:3, time2:3}
    if jogo_ida[0]<jogo_ida[1] and jogo_volta[1]>jogo_volta[0]:
        return {time1:3, time2: 3}
    if jogo_ida[0]>jogo_ida[1] and jogo_volta[1]==jogo_volta[0]:
        return {time1:4, time2:1}
    if jogo_ida[0==jogo_ida[1] and jogo_volta[1]>jogo_volta[0]:
                return {time1:4, time2:1}
                if jogo_ida[0]<jogo_ida[1] and jogo_volta[1]==jogo_volta[0]:
                return {time1:1, time2:4}
                if jogo_ida[0]==jogo_ida[1] and jogo_volta[1]<jogo_volta[0]:
                return {time1:1, time2:4}