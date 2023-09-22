def bolos (A,B,C):
    '''
    função que recebe a quantidade de ingredientes
    e retorna a quantidade maxima de bolos é possivel 
    ser feito
    '''
    return min(A//2, B//3, C//5)