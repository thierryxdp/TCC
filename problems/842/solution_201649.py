def pontos_por_time(lista):
    jogo_ida = lista[0]
    jogo_volta = lista[1]
    
    time_ida_0 = jogo_ida[0] #nome time 0
    gols_ida_0 = jogo_ida[2][0]
    
    time_ida_1 = jogo_ida[1] #nome time 1
    gols_ida_1 = jogo_ida[2][1]
    
    time_volta_0 = jogo_volta[0] #nome time 1
    gols_volta_1 = jogo_volta[2][0]
    
    time_volta_1 = jogo_volta[1] #nome time 0
    time_volta_1 = jogo_volta[2][1]
   
    pontos_0 = 0
    pontos_1 = 0
    
    if gols_ida_0 > gols_ida_1:
        pontos_0 += 3
    if gols_ida_0 < gols_ida_1:
        pontos_1 += 3
    if gols_ida_0 == gols_ida_1:
        pontos_0 += 1
        pontos_1 += 1
        
    if gols_volta_0 > gols_volta_1:
        pontos_1 += 3
    if gols_volta_0 < gols_volta_1:
        pontos_0 += 3
    if gols_volta_0 == gols_volta_1:
        pontos_0 += 1
        pontos_1 += 1
     
    return {time_ida_0:pontos_0,time_ida_1:pontos_1}