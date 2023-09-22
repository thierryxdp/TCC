def bolos(A,B,C):
    '''Dadas as quantidades de xícaras de farinha de 
    trigo (A), ovos (B) e colheres de sopa de leite (C), a 
    função retorna a quantidade máxima de bolos que se pode
    fazer. int, int, int -> int'''
    return min(A//2,B//3,C//5)