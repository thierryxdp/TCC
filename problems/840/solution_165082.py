def bolos(A,B,C):
    ''' Calcula e retorna a quantidade máxima de bolos inteiros que João pode fazer, quando informados a quantidade de: xícaras de farinha de trigo(A), de ovos(B) e de colheres de sopa de leite(C)'''
    return min(A//2,B//3,C//5)