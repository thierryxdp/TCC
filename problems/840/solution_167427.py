def bolos(A, B, C):
    """Calcula a quantidade de bolos que e possivel fazer;
    Dado a quantidade de ingredientes de entrada:
    Xícaras de Farinha (A), Ovos (B), Colheres de sopa de Leite (C).
    int, int, int -> int """
    if (A/2)<(B/3) and (A/2)<(C/5):
        return (A/2)
    elif (B/3)<(A/2) and (B/3)<(C/5):
        return (B/3)
    elif (C/5)<(A/2) and (C/5)<(B/3):
        return (C/3)
    else:
        return 0