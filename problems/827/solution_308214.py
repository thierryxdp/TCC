def qtd_divisores(num):
    divisores = 0
    for numeros in range(1,num+1):
        if num%numeros == 0:
            divisores += 1
    return divisores