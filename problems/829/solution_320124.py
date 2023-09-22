def soma_h(n):
    """função calcula H = 1 + 1/2 + 1/3 + ... 1/N, onde N é dado como entrada.
    int -> float"""
    soma = 0
    for c in range(1, n + 1):
        inverso = (1/c)
        soma += inverso
    return round(soma, 2)