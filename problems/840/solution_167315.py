def bolos(A, B, C):
    """Calcula a quantidade de bolos que e possivel fazer;
    Dados as quantidades de ingredientes de entrada:
    Xícaras de Farinha (A), Ovos (B), Colheres de sopa de Leite (C).
    int, int, int -> int """
    return int(((A/2)+(B/3)+(C/5))/3)