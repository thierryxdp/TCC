#Start your python function here
def pontos_por_time(jogos):
    '''Função que recebe como entrada uma lista de 2 elementos, onde cada um desses elementos
    também é uma lista com 3 elemetos cada, sendo a primeira referente ao jogo de ida
    entre dois times em um campeonato de futebol e a segunda referente ao jogo de volta.
    Os 3 elementos da lista são duas strings com o nome dos dois times e uma lista com o
    numero de gols que cada time marcou(a ordem da quantidade de gols deve ser igual a ordem
    dos nomes dos times). A função retorna um dicionário cujos mapeamentos são:<nome do time> ->
    <numeros de pontos na fase>.Os pontos de um time na fase são calculados da seguinte forma:
    em cada jogo, os times recebem três pontos por vitória e um ponto por empate, e não são atribuídos
    pontos para derrotas. lista->dicionário'''
    nome_time1=jogos[0][0]
    nome_time2=jogos[0][1]
    gols_time1_ida= jogos[0][2][0]
    gols_time2_ida=jogos[0][2][1]
    gols_time1_volta=jogos[1][2][1]
    gols_time2_volta=jogos[1][2][0]
    if gols_time1_ida>gols_time2_ida:
        pontos_time1_ida=3
        pontos_time2_ida=0
    elif gols_time1_ida<gols_time2_ida:
        pontos_time1_ida=0
        pontos_time2_ida=3
    elif gols_time1_ida==gols_time2_ida:
        pontos_time1_ida=1
        pontos_time2_ida=1
    if gols_time1_volta>gols_time2_volta:
        pontos_time1_volta=3
        pontos_time2_volta=0
    elif gols_time1_volta<gols_time2_volta:
        pontos_time1_volta=0
        pontos_time2_volta=3
    elif gols_time1_volta==gols_time2_volta:
        pontos_time1_volta=1
        pontos_time2_volta=1
    return {nome_time1:pontos_time1_ida + pontos_time1_volta, nome_time2:pontos_time2_ida + pontos_time2_volta}