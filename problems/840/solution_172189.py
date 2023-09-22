def bolos(A, B, C):
    '''ESSA FUNCAO DIVIDE OS INGREDIENTES'''
    farinha = A//2 
    ovos = B//3
    leite = C//5
    
    quantidade = min (farinha, ovos, leite)
    return quantidade