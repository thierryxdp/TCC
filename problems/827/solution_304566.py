def qtd_divisores(n):
    """Calcula a quantidade de divisores tem um numero e os retorna."""
    for numeros in range(0,n+1):
        if numeros % n == 0:
            soma = sum(numeros)
    return soma