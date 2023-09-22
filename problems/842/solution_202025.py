def pontos_por_time(lista):
    """função que recebe uma lista de dois elementos, onde cada elemento é também uma lista
    onde essas 2 listas servem de parâmetro para calcular o n° de pontos feitos na partida
    de ida e volta dos times Cormengo e Flamínthians, a função retorna o ponto dos mesmos
    por meio de um dicionário;
    list -> dict"""
    jogo1 = lista[0]
    jogo2 = lista[1]
    time1 = jogo1[0]
    time2 = jogo2[0]
    pontost1 = 0
    pontost2 = 0
    if jogo1[2][0] > jogo1[2][1]:
        pontost1 + 3 
        pontost2 + 0
    elif jogo1[2][0] < jogo1[2][1]:
        pontost1 + 0 
        pontost2 + 3
    elif jogo1[2][0] == jogo1[2][1]:
        pontost1 + 1
        pontost2 + 1
    if jogo2[2][0] > jogo2[2][1]:
        pontost1 + 0 
        pontost2 + 3
    elif jogo2[2][0] < jogo2[2][1]:
        pontost1 + 3
        pontost2 + 0
    elif jogo2[2][0] == jogo2[2][1]:
        pontost1 + 1
        pontost2 + 1
        return {time1:pontost1, time2:pontost2}