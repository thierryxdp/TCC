def bolos(A, B, C):
    '''
    Calcula quantos maxima de bolos se pode fazer dados os ingredientes A, B e C.
    int, int, int -> int
    '''
    return min(A//2, B//3, C//5)