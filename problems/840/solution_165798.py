def bolos(A,B,C):
    """Calcula e retorna a quantidade máxima de bolos que João consegue fazer, sendo:
    A= farinha de trigo;
    B= ovos;
    C= leite
    int, int -> int"""
    return min(A//2,B//3,C//5)