def bolos (A, B, C):
    '''função que retorna o número máximo de bolos que João consegue fazer dadas as medidas que ele possui em casa de xícaras de farinha de trigo (A), números de ovos (B) e colheres de sopa de leite (C);
    int, int, int -> int'''
    Trigo = A/2
    Ovos = B/3
    Leite = C/5
    return min(Trigo, Ovos, Leite)