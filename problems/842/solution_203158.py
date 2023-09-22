def pontos_por_time(jogos):
    '''retorna uma dicionario contendo o nome dos times como chave e como valor o total de pontos obtidos pelos mesmo na rodada
    list -> dict'''
    time1 = jogos[0][0]
    time2 = jogos[0][1]
    
    pontos = {time1:0,time2:0}
    
    jogo_ida = jogos[0]
    jogo_volta = jogos[1]
    
    if jogo_ida[2][0] > jogo_ida[2][1]:
        pontos[time1] = pontos[time1] + 3
    elif jogo_ida[2][1] > jogo_ida[2][0]:
        pontos[time2] = pontos[time2] + 3
    else:
        pontos[time2] = pontos[time2] + 1
        pontos[time1] = pontos[time1] + 1
        
    if jogo_volta[2][0] > jogo_volta[2][1]:
        pontos[time1] = pontos[time1] + 3
    elif jogo_volta[2][1] > jogo_volta[2][0]:
        pontos[time2] = pontos[time2] + 3
    else:
        pontos[time2] = pontos[time2] + 1
        pontos[time1] = pontos[time1] + 1
    
    return pontos