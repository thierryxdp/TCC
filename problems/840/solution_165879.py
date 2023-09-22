def bolos(A,B,C):
    '''
    calcula quantos bolos podem ser feitos com A xícaras
    de farinha de trigo, B ovos e C colheres de sopa de 
    leite
    : param A: float
    : param B: float
    : param C: float
    : return : int
    '''
    return min(A//2,B//3,C//5)