def bolos(A,B,C):
    """retorna a quatidade de bolos que Joao
    consegue fazer com os ingredientes disponiveis
    sendo eles, A (xicaras de farinha), B (ovos) e
    C (colheres de sopa de leite).
    int, int, int -> int"""
    return min((A//2),(B//3),(C//5))