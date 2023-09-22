def soma_h(n):
    """Calcula s serie harmonica de N, dado: N
    (inteiro)"""
    soma = 0
    for i in range(1, n+1):
        soma += 1.0/i
    return soma