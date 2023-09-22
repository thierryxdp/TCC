def pontos_por_time (jogoi,jogov):
    '''funcao que retorne um dicionario com nome do time e numero total de pontos na fase'''
    nome_t1=jogoi[0]
    nome_t2=jogov[0]
    pontos_t1=jogoi[0][0]+ jogov[0][1]
    pontos_t2=jogoi[0][1]+ jogov[0][0]
    return {nome_t1:pontos_t1, nome_t2:pontos_t2}