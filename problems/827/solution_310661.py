def qtd_divisores(x):
    for n in range(1,x):
        if x%n == 0:
            return str (n)