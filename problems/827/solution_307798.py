def qtd_divisores(n):
    qtd = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            qtd = qtd + divisor
    return qtd