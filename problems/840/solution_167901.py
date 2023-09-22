def bolos(A,B,C):
    """calcula a quantidade de bolos que podem ser produzidos, dado a quantidade de ingredientes,
sendo A xícaras detem A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite."""
    return min(A//2,B//3,C//5)