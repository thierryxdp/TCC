def qtd_divisores(num):
    divisores = 0
    for numero in range(1,num+1):
        if num % numero == 0:
            divisores += 1
    return divisores