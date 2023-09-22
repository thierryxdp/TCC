def pontos_por_time(jogos):
    """ Dados o número de gols de duas partidas entre dois times, determina a pontuação de cada um desses dois times 
    list -> dict """
    gols1 = jogos[0][2][0]
    gols2 = jogos[0][2][1]
    pontos1,pontos2 = 0,0
    if gols1>gols2:
        pontos1=3
    if gols1<gols2:
        pontos2=3
    if gols1==gols2:
        pontos1,pontos2=1,1

    pontuacaoTotal = {jogos[0][0]:pontos1, jogos[0][1]:pontos2}

    gols1 = jogos[1][2][0]
    gols2 = jogos[1][2][1]
    pontos1,pontos2 = 0,0
    if gols1>gols2:
        pontos1=3
    if gols1<gols2:
        pontos2=3
    if gols1==gols2:
        pontos1,pontos2=1,1

    pontuacaoTotal[jogos[1][0]] +=pontos1
    pontuacaoTotal[jogos[1][1]] +=pontos2
    return pontuacaoTotal