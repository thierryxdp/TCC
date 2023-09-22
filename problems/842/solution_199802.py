#Start your python function here
postos por time:
def pontos_por_time(J):
    
    '''
    Essa função deve calcular de cada possibilidade de placar, 
    sendo:
    vitoria / derrota
    vitoria / vitoria
    derrota / derrota
    empate / empate
    vitoria / empate
    '''
    
    if J[0][2][0] > J [0][2][1] and J [1][2][1] > J[1][2][0]:
        return {J[0][0]: 6, J[0][1]: 0}
    
    elif J[0][2][0] == J [0][2][1] and J [1][2][1] == J[1][2][0]:
        return {J [0][0]: 2, J[0][1]: 2}
    elif J[0][2][0] > J[0][2][1] and J[1][2][0] > J[1][2][1]:
        return {J[0][0]: 3, J[0][1]: 3}
    elif J[0][2][0] < J[0][2][1] and J[1][2][1] < J[1][2][0]:
        return {J[0][0]: 0, J[0][1]: 6}
    elif J[0][2][0] < J[0][2][1] and J[1][2][1] > J[1][2][0]:
        return {J[0][0]: 3, J[0][1]: 3}
    elif J[0][2][0] < J[0][2][1] and J[1][2][1] == J[1][2][0]:
        return {J[0][0]: 1, J[0][1]: 4}
    else:
         return {J[0][0]: 1, J[0][1]: 4}