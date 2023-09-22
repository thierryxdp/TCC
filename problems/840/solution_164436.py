def bolos (A,B,C):
    '''Calcula a quantidade de bolos inteiros que é possível fazer a partir de
    A xicaras de farinha de trigo,B ovos e C colheres de sops de leite'''
    A1 = A//2
    B1 = B//3
    C1 = C//5
    return min(A1,B1,C1)