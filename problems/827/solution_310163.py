def qtd_divisores (numero):
    for divisor in range(1, numero/2):
        if numero % divisor == 0:
            return divisor