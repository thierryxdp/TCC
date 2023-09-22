def qtd_divisores(num):
    '''Funcao que conta quantos divisores o numero num,
    que e passado como entrada, tem.
    int -> int'''
    soma = 0

    for d in range(1,num+1):
        if num % d == 0:
            soma = soma + 1
    return soma