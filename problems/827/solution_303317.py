def qtd_divisores(n):
    '''Calcula quantos divisores um número n tem
    float -> int'''
    divisores = 1
    for numeros in n:
        if n % numeros = 0:
            divisores = divisores + 1
    return divisores