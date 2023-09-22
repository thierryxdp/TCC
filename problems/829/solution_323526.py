def soma_h(N):
    """Funcao que calcula e retorna o valor da soma do inverso 
    de N termos
    int --> float"""
    H = 0
    for i in range(1, N+1):
        H = H + 1/i
    return round(H,2)