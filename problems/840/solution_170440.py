def bolos(A, B, C):
    """Função que determina a quantidade máxima de bolos
    que se consegue fazer, dados como entrada a quantidade
    de xícaras de farinha de trigo, ovos e colheres de sopa
    de leite respectivamente. Sabendo que para se fazer um
    bolo devem ser usadas 2 xícaras de farinha de trigo, 3
    ovos e 5 colheres de sopa de leite.
    int, int, int -> int"""
    return min(A//2, B//3, C//5)