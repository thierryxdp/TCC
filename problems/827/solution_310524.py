def qtd_divisores(num):
    i = []
    for i in range(1, num + 1):
        if (num % i) == 0:
            return (len(i))