def pontos_por_time(jogos):
    jogo1 = jogos[0]
    jogo2 = jogos[1]
    times = jogo1[0:2]
    placar1 = jogo1[2]
    placar2 = jogo2[2]
    pontos_time1 = []
    pontos_time2= []
    
    if placar1[0]>placar1[1]:
        pontos_time1 = [3,0]
    if placar1[0]<placar1[1]:
        pontos_time1 = [0,3]
    else:
        pontos_time1 = [1,1]
        
    if placar2[0]>placar2[1]:
        pontos_time2 = [3,0]
    if placar2[0]<placar2[1]:
        pontos_time2 = [0,3]
    else:
        pontos_time2 = [1,1]
        
    pontos = (pontos_time1[0] + pontos_time2[1]), (pontos_time1[1] + pontos_time2[0])
    placar = {times[0]:pontos[0],times[1]:pontos[1]}
    return placar