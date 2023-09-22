def bolos(A,B,C):
    """Calcula a quantidade máxima de bolos que João consegue
    fazer dado o número de xícaras de farinha de trigo, de ovos
    e de colheres de sopa de leite que João possui; int, int, int -> int."""
    return round(A//2+B//3+C//5)