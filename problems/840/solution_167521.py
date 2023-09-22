def bolos(A,B,C):
    '''função que retorna a quantidade máxima de bolos que
    João consegue fazer dados A números de xícaras de farinha de trigo,
    B número de ovos e C número de colheres de sopa'''
    return min(A//2,B//3,C//5)