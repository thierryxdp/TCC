def pontos_por_time(jogos):
    """
    """
    jogo1 = jogos[0]
    times1 = jogo1[0]
    pontos1 = jogo1[2]
    l = dict(zip([times1[0],times1[1]],jogo1[2]))
    return l