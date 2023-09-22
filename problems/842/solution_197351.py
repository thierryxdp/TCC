def pontos_por_time(jogos):
    """
    """
    jogo1 = jogos[0]
    time1 = jogo1[0]
    time2 = jogo1[1]
    pontos1 = jogo1[2]
    l = dict(zip([time1,time2],jogo1[2]))
    return l