def qtd_divisores (numero):
    for divisor in range(1, numero+1):
        if numero % divisor == 0:
            divisor = divisor + 1
    return divisor