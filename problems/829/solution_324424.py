def soma_h(N):
    """Retorna a soma de N numeros de uma fracao 1/N;
    int --> float"""

    buffer_float = 0

    for iii in range(0, N):
        buffer_float += 1/iii

    return round(buffer_int, 2)