def pontos_por_time(*jogos):
    ''' função que entrega a pontuação dos times após o
    	o resultado dos jogos de ida e de volta
        list(list, list) --> dict'''
    jogos = list(jogos)
    jogo_ida = jogos[0][0]
    jogo_volta = jogos[0][1]
    
    gols_jogos_ida = jogo_ida[2]
    gols_jogos_volta = jogo_volta[2]
    
    time1 = jogo_ida[0]
    time2 = jogo_ida[1]
    
    if gols_jogos_ida[0] > gols_jogos_ida[1] and gols_jogos_volta[0] < gols_jogos_volta[1]:
        return {time1 : 6 , time2 : 0}
    elif gols_jogos_ida[0] > gols_jogos_ida[1] and gols_jogos_volta[0] == gols_jogos_volta[1]:
        return {time1 : 4, time2 : 1}
    elif gols_jogos_ida[0] > gols_jogos_ida[1] and gols_jogos_volta[0] > gols_jogos_volta[1]:
        return {time1: 3, time2: 3}
    elif gols_jogos_ida[0] == gols_jogos_ida[1] and gols_jogos_volta[0] > gols_jogos_volta[1]:
        return {time1: 1, time2: 3}
    elif gols_jogos_ida[0] < gols_jogos_ida[1] and gols_jogos_volta[0] > gols_jogos_volta[1]:
        return {time1: 0, time2: 6}
    elif gols_jogos_ida[0] < gols_jogos_ida[1] and gols_jogos_volta[0] < gols_jogos_volta[1]:
        return {time1: 3, time2:3}
    elif gols_jogos_ida[0] == gols_jogos_ida[1] and gols_jogos_volta[0] == gols_jogos_volta[1]:
        return {time1: 2, time2: 2}
    else:
        return ('abc')