def qtd_divisores():
    "Contando divisores do número inserido."
    divisor = 1
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            return divisor