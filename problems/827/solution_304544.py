def qtd_divisores(numero):
    divisor = 0
    for contador in range(1,numero+1):
        if (numero%contador) == 0:
            divisor += 1
        return divisor