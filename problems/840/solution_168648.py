def bolos(A, B, C):
    """Função que calcula a quantidade máxima de bolos que pode ser feito, dados respectivamente as xícara de farinha
    de trigo disponíveis, a quantidade de ovos e as colheres de sopa de leite."""
    return min(A//2, B//3, C//5)