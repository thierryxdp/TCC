def pontos_por_time (jogoi,jogov):
    '''funcao que retorne nome do time e numero total de pontos na fase'''
    '''list, list --> dict'''
    t1=jogoi[0]
    t2=jogov[0]
    pontost1= jogoi[2][0]+ jogov[2][1]
    pontost2= jogoi[2][1]+ jogov[2][0]
    return (jogoi[0]:pontost1, jogov[0]:pontost2)