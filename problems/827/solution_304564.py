def qtd_divisores(n):
    """Calcula a quantidade de divisores tem um numero e os retorna."""
    soma = 0
    for numeros in range(1,n+1):
        if numeros % n == 0:
            soma += numeros
        if numeros == 1 or numeros == n:
            soma = soma +1 +n
    return soma