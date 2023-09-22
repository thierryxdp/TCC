import math
def bolos (A,B,C):
    """retorna o número máximo de bolos dados a quantidade de xícaras de farinha de trigo,ovos e colheres de sopa de leite respectivamente."""
    return min(A//2,B//3,C//5)