def qtd_divisores(num):
    '''Função que conta quantos divisores o um numero tem.
    int -> int'''

    divisores = 0
    
    for d in range(1,num):
        if num % d == 0:
            divisores = divisores + 1
    return divisores