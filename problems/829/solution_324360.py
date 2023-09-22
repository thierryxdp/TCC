def soma_h(N):
    """Recebe um número inteiro, retorna a soma de 1 + 1/N
    int -> float"""
    y = 0
    for x in range(1, N+1):
        y = y + 1/x
    return round(y, 2)