def soma_h(N):
    """
    Essa função recebe um número inteiro e retorna a soma de H;
    int -> bool
    """
    numero = 1
    for i in range(2, N):
        numero += 1/i
    return round(numero, 2)