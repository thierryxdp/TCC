def bolos(A, B, C):
    """Calcula o número máximo de bolos que é possível fazer, dado a quantidade de 
    xícaras de farinha (A), ovos (B) e colheres de sopa de leite (C).
    obs: 1 receita de bolo utiliza 2 xícaras de farinha, 3 ovos e 5 colheres de sopa 
    de leite.
    int, int, int -> int"""
    return min(A//2, B//3, C//5)