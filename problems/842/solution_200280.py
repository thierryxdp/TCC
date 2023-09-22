def pontos_por_time(l):
    '''
    '''
    if l[0][2][0] > l[0][2][1] and l[1][2][0] > l[1][2][1]:
        return {l[0][0]: 6, l[0][1]: 0}
    else:
        return 0