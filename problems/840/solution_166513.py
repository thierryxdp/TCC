def bolos(A,B,C):
    '''Funçao que calcula a quantidade de bolos possiveis de serem feitos a partir da quantidade de ingredientes
        disponiveis;
        Int, Int, Int -> Int'''
    return min(A//2,B//3,C//5);