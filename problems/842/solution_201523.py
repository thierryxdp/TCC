def pontos_por_time(lista):
    """ entra com os nomes dos times e gols dos jogos, e retorna
    dicionario com os nomes e os pontos. list -> dic """
    nome_time1 = lista[0][0]
    nome_time2 = lista[0][1]
    ponto_time1 = 0
    ponto_time2 = 0
    if lista[0][2][0] > lista[0][2][1]:
        ponto_time1 = ponto_time1 + 3
    if lista[0][2][0] < lista[0][2][1]:
        ponto_time2 = ponto_time2 + 3
    if lista[0][2][0] is lista[0][2][1]:
        ponto_time1 = ponto_time1 + 0
        ponto_time2 = ponto_time2 + 0
    if lista[1][2][0] > lista[1][2][1]:
        ponto_time1 = ponto_time1 + 3
    if lista[1][2][0] < lista[1][2][1]:
        ponto_time2 = ponto_time2 + 3
    if lista[1][2][0] is lista[1][2][1]:
        ponto_time1 = ponto_time1 + 0
        ponto_time2 = ponto_time2 + 0
    return {nome_time1: ponto_time1, nome_time2: ponto_time2}
#Start your python function here