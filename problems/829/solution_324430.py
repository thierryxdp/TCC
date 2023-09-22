def soma_h (n):
    """calcula a soma com o número de termos dado na entrada. int-> float"""
    soma= 0
    for n in range(1, n+1):
        soma += ((-1)**n)/((2*n) +1)
    return soma