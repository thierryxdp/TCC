def bolos(A,B,C):
    ''' calcula o número de bolos que se é possivel fazer dado a quantidade inteira dos ingredientes A, xícaras de farinha de trigo,
    B ovos e C coleres de sopa de leite'''
    return min(A//2,B//3,C//5)