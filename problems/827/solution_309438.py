def qtd_divisores(n):
    '''Retorna a quantidade de divisores de um numero n
    int --> int'''
    if n < 1:
        return 1
    somaDiv = 1
    for numero in range(1,n):
        if(n % numero) == 0:
            somaDiv += 1
    return somaDiv+1