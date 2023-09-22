def pontos_por_time(jogos):
    '''
    Recebe uma lista jogos=[jogo_ida,jogo_volta] onde cada lista jogo_ida, jogo_volta
    contém o nome dos times que jogaram e os gols de cada jogo, 
    e retorna um dicionário com quantos pontos cada time fez.
    '''
    time1=jogos[0][0]
    time2=jogos[0][1]
    gols1_ida, gols2_ida, gols1_volta, gols2_volta= jogos[0][2][0], jogos[0][2][1], jogos[1][2][1], jogos[1][2][0]
    pontos1, pontos2= 0, 0
    if gols1_ida>gols2_ida:
        pontos1=pontos1+3
    elif gols1_ida==gols2_ida:
        pontos1=pontos1+1
        pontos2=pontos2+1
    else:
        pontos2=pontos2+3
    if gols1_volta>gols2_volta:
        pontos1=pontos1+3
    elif gols1_volta==gols2_volta:
        pontos1=pontos1+1
        pontos2=pontos2+1
    else:
        pontos2=pontos2+3
    return {time1:pontos1, time2:pontos2}