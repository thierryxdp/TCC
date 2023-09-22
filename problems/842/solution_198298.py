def pontos_por_time(jogos):
    '''Funçao recebe dados de dois jogos dntre dois times e retona um dicionàrio contendo o nome e a pontuaçõa dps dois times
lista -> dicionario'''
    jogoIda = jogos[0]
    jogoVolta = jogos[1]
    pontuacao1 = jogoIda[2]
    pontIda1 = pontuacao1[0]
    pontIda2 = pontuacao1[1]
    time1Ida = jogoIda[0]
    time2Ida = jogoIda[1]
    pontuacao2 = jogoVolta[2]
    pontVolta1 = pontuacao2[0]
    pontVolta2 = pontuacao2[1]
    time1Volta = jogoVolta[0]
    time2Volta = jogoVolta[1]
    if (time1Ida == time1Volta):
        if (pontIda1 > pontIda2 and pontVolta1 > pontVolta2):
            resultado = {time1Ida: 6, time2Ida:0}
        elif (pontIda1 < pontIda2 and pontVolta1 > pontVolta2) or (pontIda1 > pontIda2 and pontVolta1 < pontVolta2):
            resultado = {time1Ida: 3, time2Ida:3}
        elif ((pontIda1 == pontIda2 and pontVolta1 > pontVolta2) or (pontIda1 > pontIda2 and pontVolta1 == pontVolta2)):
            resultado = {time1Ida: 4, time2Ida:1}
        elif ((pontIda1 == pontIda2 and pontVolta1 < pontVolta2) or (pontIda1 < pontIda2 and pontVolta1 == pontVolta2)):
            resultado = {time1Ida: 1, time2Ida:4}
        elif ((pontIda1 == pontIda2 and pontVolta1 == pontVolta2) or (pontIda1 == pontIda2 and pontVolta1 == pontVolta2)):
            resultado = {time1Ida: 2, time2Ida:2}
    if (time1Ida == time2Volta):
        if (pontIda1 > pontIda2 and pontVolta2 > pontVolta1):
            resultado = {time1Ida: 6, time2Ida:0}
        elif (pontIda1 < pontIda2 and pontVolta2 > pontVolta1) or (pontIda1 > pontIda2 and pontVolta2 < pontVolta1):
            resultado = {time1Ida: 3, time2Ida:3}
        elif ((pontIda1 == pontIda2 and pontVolta2 > pontVolta1) or (pontIda1 > pontIda2 and pontVolta2 == pontVolta1)):
            resultado = {time1Ida: 4, time2Ida:1}
        elif ((pontIda1 == pontIda2 and pontVolta2 < pontVolta1) or (pontIda1 < pontIda2 and pontVolta2 == pontVolta1)):
            resultado = {time1Ida: 1, time2Ida:4}
        elif ((pontIda1 == pontIda2 and pontVolta2 == pontVolta1) or (pontIda1 == pontIda2 and pontVolta2 == pontVolta1)):
            resultado = {time1Ida: 2, time2Ida:2}
    return resultado#Start your python function here