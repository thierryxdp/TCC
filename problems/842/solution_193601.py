def pontos_por_time(jogos):
    '''Função que recebe uma lista com dois elementos, os
    quais também são listas e representam uma o jogo de ida
    e outra o jogo de volta entre dois time, e contém dentro
    de cada um os nomes dos times em termos separados da lista
    e uma outra sublista com os pontos respectivos de cada
    time
    [[str, str, [int, int]], [str, str, [int, int]]] -> {dict}'''
    jogo_1 = jogos[0]
    jogo_2 = jogos[1]
    pontos_time_1 = 0
    pontos_time_2 = 0
    jogo_1_gols = jogo_1[2]
    jogo_2_gols = jogo_2[2]
    nome_time_1 = jogo_1[0]
    nome_time_2 = jogo_1[1]
    if jogo_1_gols[0] > jogo_1_gols[1]:
        pontos_time_1 = pontos_time_1 + 3
    elif jogo_1_gols[0] < jogo_1_gols[1]:
        pontos_time_2 = pontos_time_2 + 3
    else:
        pontos_time_1 = pontos_time_1 + 1
        pontos_time_2 = pontos_time_2 + 1
    
    if jogo_2_gols[0] > jogo_2_gols[1]:
        pontos_time_2 = pontos_time_2 + 3
    elif jogo_2_gols[0] < jogo_2_gols[1]:
        pontos_time_1 = pontos_time_1 + 3
    else:
        pontos_time_1 = pontos_time_1 + 1
        pontos_time_2 = pontos_time_2 + 1
    
    if pontos_time_1 >= ponto_time_2:
    	dicionario = {nome_time_1 : pontos_time_1, nome_time_2: pontos_time_2}
    	return dicionario
    else:
        dicionario = {nome_time_2: pontos_time_2, nome_time_1 : pontos_time_1}
    	return dicionario