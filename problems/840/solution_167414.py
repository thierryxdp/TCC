def bolos(A, B, C):
    """Calcula a quantidade de bolos que e possivel fazer;
    Dado a quantidade de ingredientes de entrada:
    Xícaras de Farinha (A), Ovos (B), Colheres de sopa de Leite (C).
    int, int, int -> int """
    a = int(A/2)
    b = int(B/3)
    c = int(C/5)
    if A<=B and A<=C:
        return a
    elif B<=A and B<=C:
        return b
    else:
        return c