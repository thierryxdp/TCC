def bolos(A, B, C):
    '''função que retorna a quantidade máxima de bolos que pode ser feita,
    dada a quantidade A de xícaras de trigo, B de ovos e C de colheres de 
    colheres de sopa de leite
    int, int, int -> int'''
    return min(int(A/2), int(B/3), int(C/5))