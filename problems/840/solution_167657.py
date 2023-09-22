def bolos(A,B,C):
    """calcula quantos bolos podem ser feitos com a quantidade de ingredientes oferecida;
    A = xícaras de farinha de trigo, para um bolo precisa de 2
    B = ovos, para um bolo precisa de 3
    C = colheres de sopa de leite, para um bolo precisa de 5
    int,int,int -> int"""
    return min(A//2,B//3,C//5)