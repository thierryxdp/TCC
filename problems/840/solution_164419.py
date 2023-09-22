def bolos(A, B, C):
    '''Calcula a quantidade de bolos que podem ser feitos, 
       dadas as quantidades de A xicaras de farinha de trigo,
       B ovos e C colheres de sopa de leite;
       int, int -> int'''
a= A//2
b= B//3
c=C//5
    return min(a, b, c)