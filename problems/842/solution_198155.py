def pontos_por_time(lista):
    ida = lista[0]
    volta = lista[1]
    
    time1 = ida[0]
    time2 = ida[1]
    
    pontos_time1 = 0
    pontos_time2 = 0
    
    gols_time1_ida = ida[2][0]
    gols_time2_ida = ida[2][1]
    
    if gols_time1_ida > gols_time2_ida:
        pontos_time1 += 3
    elif gols_time1_ida < gols_time2_ida:
        pontos_time2 += 3
    elif gols_time1_ida == gols_time2_ida:
        pontos_time1 += 1
        pontos_time2 += 1

    gols_time1_volta = volta[2][1]
    gols_time2_volta = volta[2][0]
    
    if gols_time1_volta > gols_time2_volta:
        pontos_time1 += 3
    elif gols_time1_volta < gols_time2_volta:
        pontos_time2 += 3
    elif gols_time1_volta == gols_time2_volta:
        pontos_time1 += 1
        pontos_time2 += 1
    return {time1:pontos_time1, time2:pontos_time2}