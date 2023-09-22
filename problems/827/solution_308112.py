def qtd_divisores(num):
    i = 1
    divisores = ()
    while i <= num:
        if num % i == 0:
            divisores = divisores + (i,)
        i = i + 1
    return len(divisores)