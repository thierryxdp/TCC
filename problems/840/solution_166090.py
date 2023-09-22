def bolos(A, B, C):
    '''Função que retorna o número máximo de bolos que
    João consegue fazer dados os valores do número de 
    xícaras de farinha(A), número de ovos(B) e o número
    de colheres de sopa de leite(c)
    int, int, int -> int'''
    return min(A//2, B//3, C//5)