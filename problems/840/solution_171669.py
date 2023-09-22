def bolos(a,b,c):
    '''Função para calcular a quantidade de bolos que podem ser preparados com a quantidade de ingredientes seguindo a receita'''
    a1=a//2
    b1=b//3
    c1=c//5
    return min(a1,b1,c1)