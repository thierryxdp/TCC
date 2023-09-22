def bolos (A,B,C):
    """retorna a quantidade máxima de bolos que podem ser feitos
    dados a quantidade de xícaras de farinha de trigo (A), 
    de ovos (B) e de colheres de sopa (C)"""
    return min((A//2),(B//3),(C//5))