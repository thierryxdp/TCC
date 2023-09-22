def qtd_divisores(numero):
    '''Funcao que conta quantos divisores um numero tem.
    int -> int'''
    
    divisores = 0

    for i in range(1, numero + 1):
        if n % i == 0:
            divisores += 1
    
    return divisores