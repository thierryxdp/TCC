qtd_divisores (numero):
    for divisor in range(1, numero+1):
        if numero % divisor == 0:
            qtd += 1
    return qtd