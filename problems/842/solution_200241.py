def pontos_por_time(lista=[]):
    '''função que retorna o resultado de um campeonato dados os numeros de gols feitos por cada time
    list->dic'''
    jogo_ida=lista[0]
    jogo_volta=lista[1]
    time1=jogo_ida[0]
    time2=jogo_ida[1]
    placar_ida=jogo_ida[2]
    placar_volta=jogo_volta[2]
    ponto1=(placar_ida[0])+(placar_volta[1])
    ponto2=(placar_ida[1])+(placar_volta[0])
    return {time1: ponto1, time2: ponto2}