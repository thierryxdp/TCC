def pontos_por_time(lista):
    '''Partida 1'''
    partida1=lista[0]
    nome_time1=partida1[0]
    nome_time2=partida1[1]
    pontos_partida1=partida1[2]
    ponto_time1_partida1=pontos_partida1[0]
    ponto_time2_partida1=pontos_partida1[1]
    '''Partida 2'''
    partida2=lista[1]
    pontos_partida2=partida2[2]
    ponto_time1_partida2=pontos_partida2[0]
    ponto_time2_partida2=pontos_partida2[1]    
    '''Pontos do time na fase'''
    #Partida 1
    if ponto_time1_partida1==ponto_time2_partida1:
        ponto_time1_jogo1=1
        ponto_time2_jogo1=1
    elif ponto_time1_partida1>ponto_time2_partida1:
        ponto_time1_jogo1=3
        ponto_time2_jogo1=0
    else:
        ponto_time1_jogo1=0
        ponto_time2_jogo1=3
    #Partida 2
    if ponto_time1_partida2==ponto_time2_partida2:
        ponto_time1_jogo2=1
        ponto_time2_jogo2=1
    elif ponto_time1_partida2>ponto_time2_partida2:
        ponto_time1_jogo2=3
        ponto_time2_jogo2=0
    else:
        ponto_time1_jogo2=0
        ponto_time2_jogo2=3
    return {nome_time1:ponto_time1_jogo1+ponto_time1_jogo2,
            nome_time2:ponto_time2_jogo1+ponto_time2_jogo2}