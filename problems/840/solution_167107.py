def bolos(A, B, C):

    '''
        informadas as quantidades disponíveis de cada ingrediente
        retorna quantos bolos João pode fazer

        float, int, float -> int
    '''

    return min(int(A/2), int(B/3), int(C/5))