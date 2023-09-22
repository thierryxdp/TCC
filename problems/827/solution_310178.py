def qtd_divisores(n):
    '''retorna a quantidade de divisores que um numero inteiro tem int - > int'''
    divisores = 0
    i = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    
    return divisores