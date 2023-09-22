def pontos_por_time (jogoi,jogov):
    '''funcao que retorne um dicionario com nome do time e numero total de pontos na fase'''
    nome_t1=jogoi[0]
    nome_t2=jogov[0]
    pontos_t1=jogoi[1][0]+ jogov[2][2]
    pontos_t2=jogoi[2][2]+ jogov[1][0]
    return {nome_t1:pontos_t1, nome_t2:pontos_t2}