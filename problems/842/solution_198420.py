#Start your python function here
def pontos_por_time(jogos):
    p_ida = jogos[0][2]
    p_volta = jogos[1][2]
    
    p_time1 = 0
    p_time2 = 0
    
    if p_ida[0] > p_ida[1]:
        p_time1 += 3
    elif p_ida[0] == p_ida[1]:
        p_time1 += 1
        p_time2 += 1
    else:
        p_time2 += 3
    
    if p_volta[0] > p_volta[1]:
        p_time2 += 3
    elif p_volta[0] == p_volta[1]:
        p_time1 += 1
        p_time2 += 1
    else:
        p_time1 += 3
        
    return {jogos[0][0]: p_time1, jogos[0][1]: p_time2}