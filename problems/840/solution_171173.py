def bolos (A, B, C):
    """retorna a quantidade de bolos inteiros são possíveis se realizar com A xícaras de farinha, B ovos e C colheres de sopa de leite"""
    return min((A//2),(B//3),(C//5))