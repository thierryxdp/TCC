def soma_h(N):
    """Funcao que calcula a soma do inverso de N termos
    int --> float"""
    H = 0
    for i in range(N):
        H = H + (N**-1)
    return H