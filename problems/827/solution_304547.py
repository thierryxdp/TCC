def qtd_divisores(n):
    """Calcula a quantidade de divisores tem um numero e os retorna."""
    soma = 0
    for numeros in n:
        if numeros % n == 0:
        soma += numeros
    return soma