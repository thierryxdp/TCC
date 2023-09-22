def pontos_por_time(jogos):
    """retorna """
    if ((jogos[0][2][1]) > (jogos[0][2][0])) and ((jogos[1][2][1]) < (jogos[1][2][0])):
        return {jogos[0][1]: 6, jogos[1][1]: 0}
    
    elif ((jogos[0][2][1]) > (jogos[0][2][0])) and ((jogos[1][2][1]) > (jogos[1][2][0])):
        return {jogos[0][1]: 3, jogos[1][1]: 3}
    
    elif ((jogos[0][2][1]) < (jogos[0][2][0])) and ((jogos[1][2][1]) < (jogos[1][2][0])):
        return {jogos[0][1]: 3, jogos[1][1]: 3}
    
    elif ((jogos[0][2][1]) < (jogos[0][2][0])) and ((jogos[1][2][1]) > (jogos[1][2][0])):
        return {jogos[0][1]: 0, jogos[1][1]: 6}
    
    elif ((jogos[0][2][1]) ==(jogos[0][2][0])) and ((jogos[1][2][1]) ==(jogos[1][2][0])):
        return {jogos[0][1]: 2, jogos[1][1]: 2}
    
    elif ((jogos[0][2][1])==(jogos[0][2][0])) and ((jogos[1][2][1])>(jogos[1][2][0])):
        return {jogos[0][0]: 4, jogos[1][0]: 1}
    
    elif ((jogos[0][2][1])<(jogos[0][2][0])) and ((jogos[1][2][1])==(jogos[1][2][0])):
        return {jogos[0][0]: 4, jogos[1][0]: 1}