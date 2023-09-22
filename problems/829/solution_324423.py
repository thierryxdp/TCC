def soma_h(N):
    """Retorna a soma de N numeros de uma fracao 1/N;
    int --> float"""

    buffer_int = 0

    for iii in range(1, N):
        buffer_int += 1/iii

    return round(buffer_int, 2)