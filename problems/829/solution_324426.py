def soma_h(N):
    """Retorna a soma de N numeros de uma fracao 1/N;
    int --> float"""

    buffer_float = 0

    for iii in range(1, N + 1):
        buffer_float += 1/iii

    return round(buffer_float, 2)