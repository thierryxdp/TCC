def bolos(A,B,C):
    """Calcula a quantidade máxima de bolos que João consegue fazer,
    dados os parâmetros A(xícaras de farinha de trigo), B(ovos) e c(colheres
    de sopa de leite);
    float,int,float->float"""
    return min(A//2,B//3,C//5)