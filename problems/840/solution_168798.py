import math
def bolos (A, B, C):
    ''' a função documenta o número máximo de bolos
    que joão consegue fazer com os ingredientes.

    int, int, int -> int '''
    
    return min(A // 2, B // 3, C // 5)