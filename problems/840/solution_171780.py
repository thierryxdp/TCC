num_bolos(A,B,C):
    '''Retorna o máximo de bolos possíveis dados, A xícaras de farinha, B ovos e C colheres de sopa de leite. int, int, int -> int'''
    return (min(A//2,B//3,C//5))