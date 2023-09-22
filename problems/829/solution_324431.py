def soma_h (n):
    """calcula a soma com o número de termos dado na entrada. int-> float"""
    soma= 0
    for x in range(1, n+1):
        soma += ((-1)**x)/((2*x) +1)
    return soma