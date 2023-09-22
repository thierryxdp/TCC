def bolos(A,B,C):
    """calcula o numero de bolos que pode ser feito dadas as quantidades 
    A de xícaras de farinha de trigo, B de ovos e C de colheres de sopa de
    leite
    int, int, int -> int"""
    return min(A//2,B//3,C//5)