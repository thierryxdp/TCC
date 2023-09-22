def pontos_por_time(lista):
    """Retorna um dicionario com o nome do time como chave, e o numero de pontos total. Entrada com duas listas, com os nomes dos times e os gols em cada jogo
    list --> dicionario"""
    ponto_time1 = 0
    ponto_time2 = 0
    time_casa1 = lista[0][0]
    gols_timecasa1 = lista[0][2][0]
    time_fora1 = lista[0][1]
    gols_timefora1 = lista[0][2][1]
    if gols_timecasa1 > gols_timefora1:
        ponto_time1 = ponto_time1 + 3
    elif gols_timefora1 > gols_timecasa1:
        ponto_time2 = ponto_time2 + 3
    else:
        ponto_time1 = ponto_time1 + 1
        ponto_time2 = ponto_time2 + 1
    time_casa2 = lista[1][0]
    gols_timecasa2 = lista[1][2][0]
    time_fora2 = lista[1][1]
    gols_timefora2 = lista[1][2][1]
    if gols_timecasa2 > gols_timefora2:
        ponto_time2 = ponto_time2 + 3
    elif gols_timefora2 > gols_timecasa2:
        ponto_time1 = ponto_time1 + 3
    else:
        ponto_time1 = ponto_time1 + 1
        ponto_time2 = ponto_time2 + 1
    dic = {time_casa1 : ponto_time1, time_fora1 : ponto_time2}
    return dic