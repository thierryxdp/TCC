def bolos (A, B, C):
    """Função calcula a quantidade de bolos que João vai fazer
    usando determinadas quantidades  de farinha de trigo,
    ovos, e leite. int, int, int -> int"""
    return max((A//2), (B//3), (C//5))