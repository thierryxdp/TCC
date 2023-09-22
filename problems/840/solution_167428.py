def bolos(A, B, C):
    """Calcula a quantidade de bolos que e possivel fazer;
    Dado a quantidade de ingredientes de entrada:
    Xícaras de Farinha (A), Ovos (B), Colheres de sopa de Leite (C).
    int, int, int -> int """
    a = int(A/2)
    b = int(B/3)
    c = int(C/5)
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c
    if c<a and c<b:
        return 0