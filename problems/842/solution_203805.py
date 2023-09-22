def pontos_por_time (jogos):
    '''Função que retorna um dicionário contendo o número de pontos de um time
    list -> dict'''
    
    time1 = jogos[0][0]
    time2 = jogos[0][1]
    gols_time1_ida = jogos[0][2][0]
    gols_time2_ida = jogos[0][2][1]
    gols_time1_volta = jogos[1][2][1]
    gols_time2_volta = jogos[1][2][0]
    
    pontos = {time1:0, time2:0}
    
    jogo_ida = jogos[0]
    jogo_volta = jogos[1]
    
    if gols_time1_ida>gols_time2_ida:
        pontos[time1] = pontos[time1] + 3
    elif gols_time1_ida<gols_time2_ida:
        pontos[time2] = pontos[time2] + 3
    else:
        pontos[time1] = pontos[time1] + 1
        pontos[time2] = pontos[time2] + 1
        
    if gols_time1_volta>gols_time2_volta:
        pontos[time1] = pontos[time1] + 3
    elif gols_time1_volta<gols_time2_volta:
        pontos[time2] = pontos[time2] + 3
    else:
        pontos[time1] = pontos[time1] + 1
        pontos[time2] = pontos[time2] + 1
        
    pontos = {time1:0, time2:0}