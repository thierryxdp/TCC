import math
def bolos(A,B,C):
    '''calcula e retorna o número de bolos que joão
    pode fazer, de acordo com os ingredientes e suas
    proporções'''
    int, int, int -> int
    return(math.ceil(min(A//2,B//3,C//5)))