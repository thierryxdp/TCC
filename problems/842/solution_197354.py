def pontos_por_time(jogos):
    """
    	Função que dá o total de pontos de uma fase entre 
        dois times.
        list(list,list) -> dict
    """
    jogo1 = jogos[0]
    time1 = jogo1[0]
    time2 = jogo1[1]
    pontos1 = jogo1[2]
    
    fase = dict(zip([time1,time2],jogo1[2]))
    return pontos1[0]