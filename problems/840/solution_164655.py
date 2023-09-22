def bolos (A,B,C):
    """ Função que calcula e retorna a quantidade máxima de bolos que João consegue fazer, sendo A, B e C os ingredientes do bolo"""
    return min(A//2,B//3,C//5)