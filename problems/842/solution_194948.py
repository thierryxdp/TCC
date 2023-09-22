def pontos_por_time(jogos):
    '''Funçao recebe dados de dois jogos dntre dois times e retona um dicionàrio contendo o nome e a pontuaçõa dps dois times
lista -> dicionario'''
    jogoIda = jogos[0]
    jogoVolta = jogos[1]  
    pontuacao1 = jogoIda[2]
    time1Ida = jogoIda[0]
    time2Ida = jogoIda[1]
    pontuacao2 = jogoVolta[2]
    time1Volta = jogoVolta[0]
    time2Volta = jogoVolta[1]
    if (time1Ida == time1Volta):
        if (pontuacao1[0] > pontuacao1[1] and pontuacao2[0] > pontuacao2[1]):
            resultado = {time1Ida: 6, time2Ida:0}
        elif (pontuacao1[0] < pontuacao1[1] and pontuacao2[0] > pontuacao2[1]) or (pontuacao1[0] > pontuacao1[1] and pontuacao2[0] < pontuacao2[1]):
            resultado = {time1Ida: 3, time2Ida:3}
        elif ((pontuacao1[0] == pontuacao1[1] and pontuacao2[0] > pontuacao2[1]) or (pontuacao1[0] > pontuacao1[1] and pontuacao2[0] == pontuacao2[1])):
            resultado = {time1Ida: 4, time2Ida:1}
        elif ((pontuacao1[0] == pontuacao1[1] and pontuacao2[0] < pontuacao2[1]) or (pontuacao1[0] < pontuacao1[1] and pontuacao2[0] == pontuacao2[1])):
            resultado = {time1Ida: 1, time2Ida:4}
        elif ((pontuacao1[0] == pontuacao1[1] and pontuacao2[0] == pontuacao2[1]) or (pontuacao1[0] == pontuacao1[1] and pontuacao2[0] == pontuacao2[1])):
            resultado = {time1Ida: 2, time2Ida:2}
    if (time1Ida == time2Volta):
        if (pontuacao1[0] > pontuacao1[1] and pontuacao2[1] > pontuacao2[0]):
            resultado = {time1Ida: 6, time2Ida:0}
        elif (pontuacao1[0] < pontuacao1[1] and pontuacao2[1] > pontuacao2[0]) or (pontuacao1[0] > pontuacao1[1] and pontuacao2[1] < pontuacao2[0]):
            resultado = {time1Ida: 3, time2Ida:3}
        elif ((pontuacao1[0] == pontuacao1[1] and pontuacao2[1] > pontuacao2[0]) or (pontuacao1[0] > pontuacao1[1] and pontuacao2[1] == pontuacao2[0])):
            resultado = {time1Ida: 4, time2Ida:1}
        elif ((pontuacao1[0] == pontuacao1[1] and pontuacao2[1] < pontuacao2[0]) or (pontuacao1[0] < pontuacao1[1] and pontuacao2[1] == pontuacao2[0])):
            resultado = {time1Ida: 1, time2Ida:4}
        elif ((pontuacao1[0] == pontuacao1[1] and pontuacao2[1] == pontuacao2[0]) or (pontuacao1[0] == pontuacao1[1] and pontuacao2[1] == pontuacao2[0])):
            resultado = {time1Ida: 2, time2Ida:2}
    return resultado