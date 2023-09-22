def qtd_divisores(n):
    """Calcula a quantidade de divisores tem um numero e os retorna."""
    for numeros in range(1,n+1):
        if numeros % n == 0:
            numeros += numeros
    return numeros