def pontos_por_time(jogos):
    '''doc'''
    pontos = {jogos[0][0]:0,jogos[0][1]:0}
    jogo_ida = jogos[0]
    jogo_volta = jogos[1]
    
    if jogo_ida[2][0] > jogo_ida[2][1]:
        pontos['Cormengo'] = pontos['Cormengo'] + 3
    elif jogo_ida[2][1] > jogo_ida[2][0]:
        pontos['Flaminthians'] = pontos['Flaminthians'] + 3
    else:
        pontos['Flaminthians'] = pontos['Flaminthians'] + 1
        pontos['Cormengo'] = pontos['Cormengo'] + 1
        
    if jogo_volta[2][0] > jogo_volta[2][1]:
        pontos['Cormengo'] = pontos['Cormengo'] + 3
    elif jogo_volta[2][1] > jogo_volta[2][0]:
        pontos['Flaminthians'] = pontos['Flaminthians'] + 3
    else:
        pontos['Flaminthians'] = pontos['Flaminthians'] + 1
        pontos['Cormengo'] = pontos['Cormengo'] + 1
    
    return pontos