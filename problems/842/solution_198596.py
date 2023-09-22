def pontos_por_time(lista):
    '''Esta funcao calcula os pontos de dois times dados dois jogos.'''
    '''list --> dict'''
    if lista[0][2][0] > lista[0][2][1] and lista[1][2][1] > lista[1][2][0]:
        return{lista[0][0]: 6, lista[0][1]: 0}
    elif lista[0][2][0] > lista[0][2][1] and lista[1][2][1] < lista[1][2][0]:
        return {lista[0][0]: 3, lista[0][1]: 3}
    elif lista[0][2][0] < lista[0][2][1] and lista[1][2][1] < lista[1][2][0]:
        return {lista[0][0]: 0, lista[0][1]: 6}
    elif lista[0][2][0] < lista[0][2][1] and lista[1][2][1] > lista[1][2][0]:
        return {lista[0][0]: 3, lista[0][1]: 3}
    elif lista[0][2][0] == lista[0][2][1] and lista[1][2][1] == lista[1][2][0]:
        return {lista[0][0]: 2, lista[0][1]: 2}
    elif lista[0][2][0] < lista[0][2][1] and lista[1][2][1] == lista[1][2][0]:
        return {lista[0][0]: 1, lista[0][1]: 4}