def bolos (A,B,C):
    """Função que calcula a quantidade de bolos que João pode fazer, tendo como base a quantidade de ingredientes que ele tem em casa
    int,int,int -> int"""
    xicaras = A//2
    ovos = B//3
    colheres = C//5
    return (xicaras, ovos, colheres)