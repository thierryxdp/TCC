def soma_h(n):
    """Calcula o valor de H com N termos;
    int -> float"""
    soma_h = 0
    for divisor in range(1, n+1):
        soma_h += 1/divisor
    return round(soma_h, 2)