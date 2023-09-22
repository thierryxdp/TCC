def bolos(A,B,C):
    """Calcula e retorna o numero maximo de bolos que Joao pode fazer,
    usando A xicaras de farinha de trigo, B ovos e C colheres de sopa de
    leite;
    int,int,int->int"""
    return min(A//2,B//3,C//5)