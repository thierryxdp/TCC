def qtd_divisores (numero):
    numero = numero/2
    for divisor in range(1, numero):
        if numero % divisor == 0:
            return divisor