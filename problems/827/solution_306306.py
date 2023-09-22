def qtd_divisores(n):
    numero_duvisores = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            numero_divisores += divisor +1
    return numero_divisores