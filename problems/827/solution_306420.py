def qtd-divisores(n):
    if n < 0:
        return 0
    soma_divisores = 0
    for numero in range (1, n):
        if (n % numero) == 0:
            soma_divisores += 1 
    return soma_divisores + 1