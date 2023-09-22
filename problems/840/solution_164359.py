def bolos(A,B,C):
    '''Calcula a quantidade maxima de bolos que podera ser produzido 
    seguindo as medidas exatas da receita, dados A xicaras de farinha
    de trigo, B ovos e C colheres de sopa de leite.
    int, int, int -> int'''
    return min(A/2,B/5,C/5)