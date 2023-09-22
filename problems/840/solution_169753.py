def bolos(A,B,C):
    '''Função que retorna a quantidade de bolos possíveis a 
    serem feitos com determinado números de ingredientes A, B e C;
    float,int,float->int'''
    return min(A//2, B//3, C//5)