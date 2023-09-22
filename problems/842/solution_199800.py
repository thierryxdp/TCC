postos por time:
def pontos_por_time(jogo):
    
    '''
    Foi feito o calculo de cada possibilidade de placar, sendo:
    vitoria / derrota
    vitoria / vitoria
    derrota / derrota
    empate / empate
    vitoria / empate
    '''
    
    if jogo[0][2][0] > jogo [0][2][1] and jogo [1][2][1] > jogo[1][2][0]:
        return {jogo[0][0]: 6, jogo[0][1]: 0}
    
    elif jogo[0][2][0] == jogo [0][2][1] and jogo [1][2][1] == jogo[1][2][0]:
        return {jogo [0][0]: 2, jogo[0][1]: 2}
    elif jogo[0][2][0] > jogo[0][2][1] and jogo[1][2][0] > jogo[1][2][1]:
        return {jogo[0][0]: 3, jogo[0][1]: 3}
    elif jogo[0][2][0] < jogo[0][2][1] and jogo[1][2][1] < jogo[1][2][0]:
        return {jogo[0][0]: 0, jogo[0][1]: 6}
    elif jogo[0][2][0] < jogo[0][2][1] and jogo[1][2][1] > jogo[1][2][0]:
        return {jogo[0][0]: 3, jogo[0][1]: 3}
    elif jogo[0][2][0] < jogo[0][2][1] and jogo[1][2][1] == jogo[1][2][0]:
        return {jogo[0][0]: 1, jogo[0][1]: 4}
    else:
         return {jogo[0][0]: 1, jogo[0][1]: 4}#Start your python function here