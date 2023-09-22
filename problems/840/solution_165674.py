def bolos(A, B, C):
    '''Calcula a quantidade máxima de bolos 
       que João consegue fazer, dados o número de:
       xícaras de farinha de trigo (A), ovos (B) e
        colheres de sopa de leite (C);
        int, int, int -> int'''
    return min((A//2), (B//3), (C//5))