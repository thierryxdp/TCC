def pontos_por_time(dados):
    jogo1 = dados[0]
    jogo2 = dados[1]
    placar1 = jogo1[1]
    placar2 = jogo2[1]
    pts1 = 0
    pts2 = 0
    if placar1[0] > placar1[1]:
 		pts1 += 3
    elif placar1[0] = placar1[1]:
        pts1 += 1
        pts2 += 1
    if placar1[0] < placar1[1]:
 		pts2 += 3
        
    if placar2[0] > placar2[1]:
 		pts1 += 3
    elif placar2[0] = placar2[1]:
        pts1 += 1
        pts2 += 1
    if placar2[0] < placar2[1]:
 		pts2 += 3 
    return {jogo1[0][0]:pts1, jogo1[0][1]:pts2}