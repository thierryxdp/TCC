def pontos_por_time(fase):
    """Recebe uma lista com dois elementos que também são listas
    contendo número de gols em dois jogos de futebol entre dois
    times e retorna um dicionário cujos mapeamentos são o nome do
    time e o número total de pontos na fase
    list -> dict"""
    
    pontos = {}
    pontos[fase[0][0]] = 0
    pontos[fase[0][1]] = 0
    
    jogo1Time1 = fase[0][2][0]
    jogo1Time2 = fase[0][2][1]
    
    if jogo1Time1 > jogo1Time2
       pontos[fase[0][0]] = 3
    elif jogo1Time2 > jogo1Time2
       pontos[fase[0][1] = 3
    else
       pontos[fase[0][0]] = 2
       pontos[fase[0][1] = 2
    
    jogo2Time1 = fase[1][2][1]
    jogo2Time2 = fase[1][2][0]
    
    if jogo2Time1 > jogo1Time2
       pontos[fase[0][0]] += 3
    elif jogo2Time2 > jogo1Time2
       pontos[fase[0][1] += 3
    else
       pontos[fase[0][0]] += 2
       pontos[fase[0][1] += 2
    return pontos