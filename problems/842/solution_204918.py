def pontos_por_time(dados):
    jogo1 = dados[0]
    jogo2 = dados[1]
    time1 = jogo1[0]
    time2 = jogo1[1]
    pts1 = 0
    pts2 = 0
    if jogo1[2][0] > jogo1[2][1]:
 		pts1 += 3
    elif jogo1[2][0]  == jogo1[2][1]:
        pts1 += 1
        pts2 += 1
    elif jogo1[2][0]  < jogo1[2][1]:
 		pts2 += 3
        
    if jogo2[2][0] > jogo2[2][1]:
 		pts2 += 3
    elif jogo2[2][0] == jogo2[2][1]:
        pts1 += 1
        pts2 += 1
    elif jogo2[2][0] < jogo2[2][1]:
 		pts1 += 3 
    return {time1:pts1, time2:pts2}