def soma_h(N):
    """Dado um número N inteiro, retorna a soma de 1 + 1/2 + 1/3... + 1/N
    int -> float"""
    acumulador = 0
    for x in range(1, N+1):
        acumulador = acumulador + 1/x
    return round(acumulador, 2)