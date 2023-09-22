def qtd_divisores(num):
    '''Função que conta quantos divisores um número (num) tem.
    int -> int'''
    divisores = 0
    for i in range(1, num + 1):
        if num % i == 0: 
            divisores = divisores + 1
    return divisores