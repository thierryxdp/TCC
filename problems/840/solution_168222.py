def bolos(A,B,C):
    '''Função que te ajuda a saber qual quantidade máxima de bolos
    que você pode fazer, a partir de: xícaras de farinha de trigo (A), ovos (B)
    e colheres de sopa de leite (c) que você possui em casa. 
    int, int, int -> int'''
    return min(A//2, B//3, C//5);