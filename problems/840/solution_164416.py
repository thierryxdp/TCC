def bolos(A, B, C):
    '''Calcula a quantidade de bolos que podem ser feitos, 
       dadas as quantidades de A xicaras de farinha de trigo,
       B ovos e C colheres de sopa de leite;
       int, int -> int'''
    return min(A//2. B//3, C//5)