def pontos_por_time (jogoi,jogov):
    '''funcao que retorne nome do time e numero total de pontos na fase'''
    '''list, list--> dict '''
    pontos_t1= jogo1[2][0] + jogov[2][1]
    pontos_t2= jogoi[2][1] + jogov[2][0]
    return (jogoi[0]:pontos_t1, jogov[0]:pontos_t2)