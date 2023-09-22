def bolos(A,B,C):
    '''Calcula o número máximo de bolos que João poderá fazer com um número A de xícaras de farinha de trigo, um número B de ovos e um número C de colheres de sopa de leite; int, int, int --> int'''
    return min((A//2),(B//3),(C//5))