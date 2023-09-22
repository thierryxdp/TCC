def pontos_por_time (jogo):
    """Funçao que me dado uma lista e resultado de dois jogos, me retorna um dicionario,
contendo a quantidade de pontos de cada time com seu respectivo nome"""
    time1=jogo[0]
    time2=jogo[0]
    gols1=jogo[2][0]+jogo[2][1]
    gols2=jogo[2][1]+jogo[2][0]
    return {time1:gols1,time2:gols2}