def qtd_divisores(num):
    for i in range(1, num//2+1):
        if num % i == 0:
            i
    return list(num)