def bolos(A.B,C):
    '''Dados os ingredientes A,B e C, retorna o número máximo de bolos que João pode fazer '''
    return (min((A/2),(B/3),(C/5))//1)