def colisao(ret1, ret2):
    '''
       Função que duas tuplas com quatro valores inteiros cada uma informa se houve ou não colisão.
       ret1: Primeira tupla
       ret2: Segunda tupla
       Saída: tuple, tuple --> bool
    '''
    x = [[0,0],[0,0]]
    y = [[0,0],[0,0]]
    
    x[0][0], y[0][0], x[0][1], y[0][1] = ret1
    x[1][0], y[1][0], x[1][1], y[1][1] = ret2
    if (x[0][1] < x[1][0]) or (x[1][1] < x[0][0]) or (y[0][1] < y[1][0]) or (y[1][1] < y[0][0]) or (x[0][0] > x[1][1]) or (x[1][0] > x[0][1]) or (y[0][0] > y[1][1]) or (y[1][0] > y[0][1]):
        return False
    else:
        return True