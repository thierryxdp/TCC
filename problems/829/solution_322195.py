def soma_h(N):
    """Funcao que calcula a soma do inverso de N termos
    int --> float"""
    valor = 0
    for i in range(N):
        valor = valor + (1/N)
        valor = round(valor, 2)
    return valor