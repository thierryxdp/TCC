def pontos_por_time(jogos):

    '''

notas pro desenvolvimento:

cada jogo -> 3 pnts por vitoria e 1 por empate
total pnts = soma dos dois jogos da fase


um parametro list com duas listas dentro
[['Cormengo','Flamínthians',[1,0]],['Flamínthians','Cormengo',[2,2]]]

retornar um dicionário {} com nome dos times e o total de pontos na fase
{'Cormengo':4, 'Flamínthians':1}

    '''
    time1 = jogos[0][0]
    time2 = jogos[0][1]
    pntsT1 = 0
    pntsT2 = 0

    #PONTOS DO PRIMEIRO JOGO:
    if jogos[0][2][0] != jogos[0][2][1]:
#não é empate = 3pnts
        if jogos[0][2][0] > jogos[0][2][1]:
            pntsT1 = pntsT1 + 3

        if jogos[0][2][0] < jogos[0][2][1]:
            pntsT2 = pntsT2 + 3
            
    else:
#empate = 1pnt
        pntsT1 = pntsT1 + 1
        pntsT2 = pntsT2 + 1

    #PONTOS DO SEGUNDO JOGO:
    if jogos[1][2][0] != jogos[1][2][1]:
#não é empate = 3pnts
        if jogos[1][2][0] > jogos[1][2][1]:
            pntsT2 = 3

        if jogos[1][2][0] < jogos[1][2][1]:
            pntsT1 = 3
            
    else:
#empate = 1pnt
        pntsT1 = pntsT1 + 1
        pntsT2 = pntsT2 + 1

    return {time1:pntsT1, time2:pntsT2}