def pontos_por_time(lista1):
    '''recebe duas listas que indicam os times e os gols na partida e retorna um dicionario que indica o nome do time e o total de pontos na fase. entrada: lista. saida: dicionario'''
    time1 = lista1[0][0]
    time2 = lista1[0][1]
    pontos1 = 0
    pontos2 = 0
    if lista1[0][2][0] > lista1[0][2][1]:
        pontos1 += 3
    elif lista1[0][2][0] == lista1[0][2][1]:
        pontos1 += 1
        pontos2 += 1
    else: 
        pontos2 += 3
    if lista1[1][2][list.index(lista1[1],time1)] > lista1[1][2][list.index(lista1[1],time2)]:
        pontos1 += 3
    elif lista1[1][2][0] == lista1[1][2][1]:
        pontos1 += 1
        pontos2 += 1
    else:
        pontos2 +=3
    dicionario = {time1:pontos1, time2:pontos2}
    return dicionario