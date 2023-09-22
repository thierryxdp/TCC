def bolos (A, B, C):
    '''funcao que calcula o numero maximo de bolos que podem ser feito, dado as quantidades de xicaras de farinha (A), de ovos (B) e de coleheres de sopa de leite (C), sabendo que para 1 bolo sao necessarias 2 xicaras de farinha de trigo, 3 vos e 5 colheres de sopa de leite
    float, float, float -> int'''
    xicaras_farinha = A//2
    ovos = B//3
    colheres_leite = C//5
    import math
    return min (xicaras_farinha, ovos, colheres_leite)