def bolos(A, B, C):
    """Dados A, B e C sendo o numero de xicaras de farinha de trigo, o numero de ovos e o numero de colheres de sopa de leite que joão tem em casa respectivamente,
    retorna a quantidade maxima de bolos que ele pode fazer, sabendo que devem ser usadas 2 xicaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite
    int, int, int -> int"""
    if A//2 <= B//3 and A//2 <= C//5:
        return A//2 
    if B//3 <= A//2 and B//3 <= C//5:
        return B//3
    if C//5 <= A//2 and C//5 <= B//3:
        return C//5