def pontos_por_time(lista):
    time1 = lista[0][0]
    time2 = lista[1][0]
    if lista[0][2][0] > lista[0][2][1]:
        pontos_t1_j1 = 3
        pontos_t2_j1 = 0
    if lista[0][2][0] == lista[0][2][1]:
        pontos_t1_j1 = 1
        pontos_t2_j1 = 1
    if lista[0][2][0] < lista[0][2][1]:
        pontos_t1_j1 = 0
        pontos_t2_j1 = 3
    if lista[1][2][0] > lista[1][2][1]:
        pontos_t1_j2 = 0
        pontos_t2_j2 = 3
    if lista[1][2][0] == lista[1][2][1]:
        pontos_t1_j2 = 1
        pontos_t2_j2 = 1
    if lista[1][2][0] < lista[1][2][1]:
        pontos_t1_j2 = 3
        pontos_t2_j2 = 0
    pontos_totais_t1 = pontos_t1_j1 + pontos_t1_j2
    pontos_totais_t2 = pontos_t2_j1 + pontos_t2_j2
    
    if (pontos_totais_t1 > pontos_totais_t2) and not (pontos_t1_j1 > pontos_t2_j1):
    	return {time1:pontos_totais_t1, time2:pontos_totais_t2}
    else:
        return {time2:pontos_totais_t2, time1: pontos_totais_t1}