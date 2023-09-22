def bolos(A,B,C):
    '''Função que retorna a quantidade máxima de bolos que joão consegue fazer, dados o número de xícaras de farinha de trigo A, o número de ovos B e o número de colheres de sopa
    de leite C.
    int, int, int -> int'''
    return (min(A//2,B//3,C//5))