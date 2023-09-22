def pontos_por_time(lista_jogo1, lista_jogo2):
    if lista_jogo1[1][0] == lista_jogo1[1][1]:
        pontos_time1 = 1
        pontos_time2 = 1
    if lista_jogo1[1][0] > lista_jogo1[1][1]:
        pontos_time1 = 3
    if lista_jogo1[1][0] < lista_jogo1[1][1]:
        pontos_time2 = 3
    if lista_jogo2[1][0] == lista_jogo2[1][1]:
        pontos_time1 = 1
        pontos_time2 = 1
    if lista_jogo2[1][0] > lista_jogo2[1][1]:
        pontos_time1 = 3
    if lista_jogo2[1][0] < lista_jogo2[1][1]:
        pontos_time2 = 3
 	return lista_jogo1