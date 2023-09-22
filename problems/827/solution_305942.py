def qtd_divisores(n):
    '''Função que dado um número de entrada retorne a 
    quantidade de divisores que tal número tem.
    int --> int.'''
    x = 1
    divisores = []
    for x in range(1,n+1):
        if n % x == 0:
            divisores.append(x)
    return len divisores