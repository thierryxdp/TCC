#def pontos_por_time(jogo1,jogo2):
    time1=jogo1[0]
    time2=jogo1[1]
    pontos={str(time1): 0, str(time2): 0}
    if jogo1[2][0] > jogo1[2][1]:
        pontos[str(time1)]= pontos[str(time1)] + 3
    if jogo1[2][0] < jogo1[2][1]:
        pontos[str(time2)]= pontos[str(time2)]+ 3
    if jogo1[2][0] == jogo1[2][1]:
        pontos[str(time1)]= pontos[str(time1)]+ 1
        pontos[str(time2)]= pontos[str(time2)]+ 1
    if jogo2[2][0] < jogo2[2][1]:
        pontos[str(time1)]= pontos[str(time1)] + 3
    if jogo2[2][0] > jogo2[2][1]:
        pontos[str(time2)]= pontos[str(time2)]+ 3
    if jogo2[2][0] == jogo2[2][1]:
        pontos[str(time1)]= pontos[str(time1)] + 1
        pontos[str(time2)]= pontos[str(time2)] + 1
    return pontos