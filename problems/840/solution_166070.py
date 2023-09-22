def bolos(A,B,C):
    '''Calcula a quantidade de bolos possíveis que podem ser feitos dadas as quantidades obtidas de ingredientes A (xícaras de farinha de trigo), B (ovos), C (colheres de sopa de leite); int, int, int -> int'''
    return min(A//2,B//3,C//5)