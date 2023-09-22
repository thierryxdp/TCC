def soma_h(N):
    """Funcao que calcula a soma do inverso de N termos
    int --> float"""
    valor = 0
    for i in range(1,N + 1):
        valor = valor + (1/N)
    return round(valor,2)