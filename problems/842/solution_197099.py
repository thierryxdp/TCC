def pontos_por_time (jogoi, jogov):
    """Funçao que me dado uma lista e resultado de dois jogos, me retorna um dicionario,
contendo a quantidade de pontos de cada time com seu respectivo nome"""
    time1=jogoi[0]
    time2=jogov[0]
    gols1=jogoi[2][0]+jogov[2][1]
    gols2=jogoi[2][1]+jogov[2][0]
    return {time1:gols1,time2:gols2}