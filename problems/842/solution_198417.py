#Start your python function here
def pontos_por_time(jogos):
    
    p_j_ida = jogos[0][2]
    p_j_volta = jogos[1][2]
    p_time1, p_time2 = 0, 0
    
    
    if p_j_ida[0] > p_j_ida[1]:
        p_time1 =+ 3
    elif p_j_ida[0] == p_j_ida[1]:
        p_time1 =+ 1
        p_time2 =+ 1
     
    if p_j_volta[0] > p_j_volta[1]:
        p_time2 =+ 3
    elif p_j_volta[0] == p_j_volta[1]:
        p_time1 =+ 1
        p_time2 =+ 1
    
    return {jogos[0][0]: p_time1, jogos[0][1]: p_time2}