def pontos_por_time(jogos):
    """retorna """
    if ((jogos[0][2][1]) > (jogos[0][2][0])) and ((jogos[1][2][1]) < (jogos[1][2][0])):
        return {jogos[1]: 6, jogos[3]: 0}
    
    elif