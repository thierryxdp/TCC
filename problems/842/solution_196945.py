def pontos_por_time(gols):
   
    ''' Função que, dadas duas listas informando
        os número de gols em dois jogos de futebol
        entre dois times, retorna um dicionário com
        o número total de pontos de cada time na fase.
        list, list -> dict '''
    
    gols1 = gols.copy()
    gols2 = gols1.copy()
    
    jogo1 = gols1.pop(0)
    jogo2 = gols2.pop(1)
    
    placar1 = jogo1[2]
    placar2 = jogo2[2]
   
    placar_jogo1 = {jogo1[0]:placar1[0], jogo1[1]:placar1[1]}
    placar_jogo2 = {jogo2[0]:placar2[0], jogo2[1]:placar2[1]}
    
    lista_times = [jogo1[0], jogo1[1], jogo2[0], jogo2[1]]
    lista_times.sort()
    
    time1 = lista_times[0]
    time2 = lista_times[2]
    
    pontos_time1_jogo1 = placar_jogo1.get(time1)
    pontos_time2_jogo1 = placar_jogo1.get(time2)
    pontos_time1_jogo2 = placar_jogo2.get(time1)
    pontos_time2_jogo2 = placar_jogo2.get(time2)
    
    pontos_fase = {time1: 0, time2: 0}
 

    if pontos_time1_jogo1 > pontos_time2_jogo1:
        pontos_fase[time1] += 3
    
    if pontos_time1_jogo1 < pontos_time2_jogo1:
        pontos_fase[time2] += 3
        
    if pontos_time1_jogo1 == pontos_time2_jogo1:
        pontos_fase[time1] += 1
        pontos_fase[time2] += 1
        
    if pontos_time1_jogo2 > pontos_time2_jogo2:
        pontos_fase[time1] += 3
    
    if pontos_time1_jogo2 < pontos_time2_jogo2:
        pontos_fase[time2] += 3
        
    if pontos_time1_jogo2 == pontos_time2_jogo2:
        pontos_fase[time1] += 1
        pontos_fase[time2] += 1
        
    return pontos_fase