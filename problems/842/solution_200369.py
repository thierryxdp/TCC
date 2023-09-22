def pontos_por_time ([jogo1, jogo2]):
    '''calcula os pontos de dois times, a partir de 2 jogos (jogo1 e jogo2) contidos em uma lista
    [list, list] -> dict'''
    time_casa = jogo1[0]
    time_fora = jogo1[1]
    if jogo1[2][0] > jogo1[2][1]:
        pontos_casa = 3
        pontos_fora = 0
    elif jogo1[2][0] == jogo1[2][1]:
        pontos_casa = 1
        pontos_fora = 1
    else:
        pontos_casa = 0
        pontos_fora = 3
       
    pontos = {time_casa = pontos_casa, time_fora = pontos_fora}
        
    time_casa = jogo2[0]
    time_fora = jogo2[1]
        
    if jogo1[2][0] > jogo1[2][1]:
        pontos_casa += 3
        pontos_fora += 0
    elif jogo1[2][0] == jogo1[2][1]:
        pontos_casa += 1
        pontos_fora += 1
    else:
        pontos_casa += 0
        pontos_fora += 3
        
	pontos[time_casa] += pontos_casa
    pontos[time_fora] += pontos_fora
    
    return pontos