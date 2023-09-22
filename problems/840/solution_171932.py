def bolos(A,B,C):
    '''
    Essa função retorna a quantidade máxima de bolos que João consegue fazer
    dados os ingredientes: A - xícaras de faringa, B - ovos e C - colheres de sopa
    de leite.
    '''
    A = A//2
    B = B//3
    C = C//5
    
    quantidade = min(A,B,C)
    return quantidade