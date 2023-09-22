def qtd_divisores(n):
    i = 1
    div = []
    for i in n:
        if (n % i) == 0:
            return i