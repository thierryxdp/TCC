def qtd_divisores(n):
    """Calcula a quantidade de divisores tem um numero e os retorna."""
    soma = 0
    for numeros in range(1,n+1):
        if n % numeros == 0:
            soma += 1
    return soma