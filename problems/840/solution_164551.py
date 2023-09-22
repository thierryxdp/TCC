def bolos(A, B, C):
    '''funcao que retorna a quantidade exata de bolos que joao pode fazer considerando
    A:xicaras de farinha de trigo, B: ovos e C: colheres de sopa de leite.
    int, int, int ->int '''
    return min(A//2,B//3,C//5)