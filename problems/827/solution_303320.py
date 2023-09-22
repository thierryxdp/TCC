def qtd_divisores(n):
    '''Calcula quantos divisores um número n tem
    float -> int'''
    divisores = 1
    j = [range(n)]
    i = 1
    for numeros in n:
        if n % j[i] == 0:
            divisores = divisores + 1
    return divisores