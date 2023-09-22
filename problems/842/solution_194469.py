def pontos_por_time(lista):
    jogo1 = lista[0]
    gols1 = jogo1[2]
    jogo2 = lista[1]
    gols2 = jogo2[2]
    time1 = jogo1[0]
    time2 = jogo1[1]
    if gols1[0] > gols1[1] and gols2[1]>gols2[0]:
        pontos1 == 6
        pontos2 == 0
    elif gols1[0] > gols1[1] and gols2[1]<gols2[0]:
        pontos1 == pontos2 ==3
    elif gols1[0] == gols1[1] and gols2[1] == gols2[0]:
        pontos1 = pontos2 == 2
    elif (gols1[0] == gols1[1] and gols2[1]>gols2[0]) or (gols1[0]>gols1[1] and gols2[1]==gols2[0]):
        pontos1 == 4
        pontos2 == 1
    elif (gols1[0] == gols1[1] and gols2[1]<gols2[0]) or (gols1[0]<gols1[1] and gols2[1]==gols2[0]):
        pontos1 == 1
        pontos2 == 4
    else:
	    pontos1 == 0
	    pontos2 == 6
    return {time1:pontos1,time2:pontos2}