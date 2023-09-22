def bolos (A, B, C):
    '''essa função divide os ingredientes'''
    A = A//2 
    B = B//3 
    C = C//5  
    quantidade = min(A, B, C)
    return quantidade