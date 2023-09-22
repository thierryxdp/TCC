def bolos(A, B, C):
    '''Número de bolos possíveis com A xícaras de farinha, B ovos e C colheres de sopa de leite (A, B, C >= 0)'''
    return min(A // 2, B // 3, C // 5)