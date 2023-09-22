def Bolos(A,B,C):
    """Tem como objetivo calcular a quantidade de bolos
    que João quer fazer dado um número de ingredientes
    int, int, int> int"""
    bolos=0
    while (A>=2) and (B>=3) and (C>=5):
        A = A-2
        B = B-3
        C = C-5
        bolos=bolos+1
    return bolos