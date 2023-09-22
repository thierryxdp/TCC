def qtd_divisores(n):
    '''conta quantos divisores tem um número;
    int -> int'''
    divisores = 0
    for numero in range(1,n+1):
        if (n % numero) == 0:
            divisores +=1
    return divisores