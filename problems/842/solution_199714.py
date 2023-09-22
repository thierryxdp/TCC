def pontos_por_time(lista):
    '''Uma funcao que retorna um dicionario contendo um time e os pontos
    na fase cujo participou, sendo vitoria = 3 pontos, emapte = 1 ponto.
    lista -> dicionario '''
    nome_do_time1 = lista[0][0]
    nome_do_time2 = lista[0][1]
    pontos_time_1 = 0
    Pontos_time_2 = 0
    if lista[0][2][0] > lista[0][2][1]:
        pontos_time_1 += 3
    if lista[0][2][0] == lista[0][2][1]:
        pontos_time_1 += 1
        pontos_time_2 += 1
    if lista[0][2][0] < lista[0][2][1]:
        pontos_time_2 += 3   
    if lista[1][2][0] > lista[1][2][1]:
        pontos_time_2 += 3
    if lista[1][2][0] == lista[1][2][1]:
        pontos_time_1 += 1
        pontos_time_2 += 1
    if lista[1][2][0] < lista[1][2][1]:
        pontos_time_1 += 3
    return {nome_do_time1: pontos_time_1}