def pontos_por_time(jogos):
    """Função que retorna os pontos feitos por dois times em dois jogos. list --> dict"""
    if (jogos[0][2][0]>jogos[0][2][1]) and (jogos[1][2][1]>jogos[1][2][0]):
        return {jogos[0][0]:6,jogos[0][1]:0}
    if (jogos[0][2][0]>jogos[0][2][1]) and (jogos[1][2][1]==jogos[1][2][0]):
        return {jogos[0][0]:4,jogos[0][1]:1}
    if (jogos[0][2][0]==jogos[0][2][1]) and (jogos[1][2][1]>jogos[1][2][0]):
        return {jogos[0][0]:4,jogos[0][1]:1}
    if (jogos[0][2][0]==jogos[0][2][1]) and (jogos[1][2][1]==jogos[1][2][0]):
        return {jogos[0][0]:1,jogos[0][1]:1}
    if (jogos[0][2][0]<jogos[0][2][1]) and (jogos[1][2][1]==jogos[1][2][0]):
        return {jogos[0][1]:4,jogos[0][0]:1}
    if (jogos[0][2][0]==jogos[0][2][1]) and (jogos[1][2][1]<jogos[1][2][0]):
        return {jogos[0][1]:4,jogos[0][0]:1}
    if (jogos[0][2][0]<jogos[0][2][1]) and (jogos[1][2][1]<jogos[1][2][0]):
        return {jogos[0][1]:6,jogos[0][0]:0}
    if (jogos[0][2][0]>jogos[0][2][1]) and (jogos[1][2][1]<jogos[1][2][0]):
        return {jogos[0][0]:3,jogos[0][1]:3}
    if (jogos[0][2][0]<jogos[0][2][1]) and (jogos[1][2][1]>jogos[1][2][0]):
        return {jogos[0][0]:3,jogos[0][1]:3}