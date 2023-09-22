def pontos_por_time(lista):
    """ Função que recebe uma lista de dois elementos, onde cada elemento é também uma lista contendo os nomes dos times e os números de gols em dois jogos de futebol. Retorna um dicionário cujos mapeamentos são: <nome do time> -> <numero total de pontos na fase>;
        list -> dicionario"""
    time1 = lista[0][0]
    time2 = lista[0][1]
    gols_time1_jogo1 = lista[0][2][0]
    gols_time1_jogo2 = lista[1][2][1]
    gols_time2_jogo1 = lista[0][2][1]
    gols_time2_jogo2 = lista[1][2][0]
    pontos_time1 = 0 
    pontos_time2 = 0
    if gols_time1_jogo1 > gols_time2_jogo1:
     pontos_time1 = pontos_time1 + 3
    if gols_time1_jogo2 > gols_time2_jogo2:
     pontos_time1 = pontos_time1 + 3
    if gols_time1_jogo1 == gols_time2_jogo1:
     pontos_time1 = pontos_time1 + 1
     pontos_time2 = pontos_time2 +  1
    if gols_time1_jogo2 == gols_time2_jogo2:
     pontos_time1 = pontos_time1 + 1
     pontos_time2 = pontos_time2 +  1
    if not(gols_time1_jogo1 > gols_time2_jogo1) and not(gols_time1_jogo2 > gols_time2_jogo2) and not(gols_time1_jogo1 == gols_time2_jogo1) and not(gols_time1_jogo2 == gols_time2_jogo2):
     pontos_time2 = 6
    else:
        pontos_time2 = pontos_time2 + 3
        return {str(time1):pontos_time1,str(time2):pontos_time2}