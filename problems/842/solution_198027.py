def pontos_por_time(jogos):
    '''Função que calcula os pontos da fase dos times de acordo com o resultado de seus dois confrontos.
    list -> dict'''
    time1 = jogos[0][0]
    time2 = jogos[0][1]
    pntsT1 = 0
    pntsT2 = 0
    total = {}

    #PONTOS DO PRIMEIRO JOGO:
    if jogos[0][2][0] != jogos[0][2][1]:
#não é empate = 3pnts
        if jogos[0][2][0] > jogos[0][2][1]:
            pntsT1 = pntsT1 + 3
            total = {time1:pntsT1, time2:pntsT2}

        if jogos[0][2][0] < jogos[0][2][1]:
            pntsT2 = pntsT2 + 3
            total = {time1:pntsT1, time2:pntsT2}
            
    else:
#empate = 1pnt
        pntsT1 = pntsT1 + 1
        pntsT2 = pntsT2 + 1
        total = {time1:pntsT1, time2:pntsT2}

    #PONTOS DO SEGUNDO JOGO:
    if jogos[1][2][0] != jogos[1][2][1]:
#não é empate = 3pnts
        if jogos[1][2][0] > jogos[1][2][1]:
            pntsT2 = pntsT2 + 3
            total = {time1:pntsT1, time2:pntsT2}

        if jogos[1][2][0] < jogos[1][2][1]:
            pntsT1 = pntsT1 + 3
            total = {time1:pntsT1, time2:pntsT2}
            
    else:
#empate = 1pnt
        pntsT1 = pntsT1 + 1
        pntsT2 = pntsT2 + 1
        total = {time1:pntsT1, time2:pntsT2}
    return total
    #return {time1:pntsT1, time2:pntsT2}