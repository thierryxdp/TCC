def qtd_divisores(n):
    '''Calcula quantos divisores um número n tem
    float -> int'''
    divisores = 0
    for i in range(n+1):
        if i!=0 and n % i == 0:
            divisores = divisores + 1
    return divisores