def soma_h(N):
    """Recebe como parâmetro o número inteiro N e retorna o valor H dado por
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
    arredondado em duas casa decimais;
    assinatura: int --> float
    Casos de teste:
    soma_h(1) == 1.0
    soma_h(10) == 2.93
    soma_h(100) == 5.19
    """
    H = 0
    for i in range(N + 1):
        if i != 0:
            H += (1 / i)
    return round(H, 2)