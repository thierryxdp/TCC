def pontos_por_time(lista):
    """ Função que recebe uma lista de dois elementos, onde cada elemento é também uma lista contendo os nomes dos times e os números de gols em dois jogos de futebol. Retorna um dicionário cujos mapeamentos são: <nome do time> -> <numero total de pontos na fase>;
        list -> dicionario"""
    time1 = lista[0][0]
    time2 = lista[0][1]
    if lista[0][0]== 'Cormengo':
        gols_time1_jogo1 = lista[0][2][0]
        gols_cormengo_jogo2 = lista[1][2][0]
        gols_flaminthians_jogo1 = lista[0][2][1]
        gols_flaminthians_jogo1 = lista[1][2][1]
        pontos_cormengo = 0 
        if gols_cormengo_jogo1 > gols_flaminthians_jogo1:
        pontos_cormengo = pontos_cormengo + 3
        if gols_cormengo_jogo2 > gols_flaminthians_jogo2:
        pontos_cormengo = pontos_cormengo + 3
        if gols_cormengo_jogo1 == gols_flaminthians_jogo1:
        pontos_cormengo = pontos_cormengo + 1
        pontos_flaminthians = 1
        if gols_cormengo_jogo2 == gols_flaminthians_jogo2:
        pontos_cormengo = pontos_cormengo + 1
        pontos_flaminthians = 1
        return {'Cormengo':pontos_cormengo,'Flaminhtians':pontos_flaminthians}