def qtd_divisores(n:int)->int:
    "Contando divisores do número inserido."
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            return divisor