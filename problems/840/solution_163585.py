def bolos(A,B,C):
    '''bolos recebe três valores inteiros e devolve um valor inteiro
    calcula o valor máximo de bolos que podem ser feitos
    int, int,  --> int'''
    x = A//2
    y = B//3
    z = C//5
    return min(x,y,z)