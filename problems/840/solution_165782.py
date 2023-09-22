def bolos(A,B,C):
    """calcula o número de bolos que João pode fazer sendo que ele tem
    em sua casa A xícaras de farinha de trigo, B ovos e C colheres de 
    sopa de leite
    int,int,int->int"""
    return min(A//2,B//3,C//5)