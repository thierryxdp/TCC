def bolos(A, B, C):
    """Calcula a quantidade de bolos que e possivel fazer;
    Dado a quantidade de ingredientes de entrada:
    Xícaras de Farinha (A), Ovos (B), Colheres de sopa de Leite (C).
    int, int, int -> int """
    if (A/2) and (B/3) and (C/5) >=1:
        return min((A/2), (B/3), (C/5))
    else:
        return 0