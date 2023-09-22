def bolos(A,B,C):
    '''Calcula a quantidade máxima de bolos que
    se podem fazer utilizando A xícaras de farinha de trigo,
    B ovos e C colheres de sopa de leite'''
    return min(A//2, B//3, C//5, 0)