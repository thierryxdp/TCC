def bolos(A, B, C):
    '''funcao que retorna o numero maximo de bolos que podem ser feitos dadas as
    quantidades A de xicaras de trigo, B de ovos e C de colheres de sopa de leite;
    int, int, int -> int'''
    return min(A//2, B//3, C//5)