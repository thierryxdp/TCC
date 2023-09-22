def qtd_divisores(numero):
    '''
    função recebe um numero inteiro e retorna a quantidade 
    de divisores que este numero tem. 
    int --> int
    '''
    divisores = 0
    for x in range(1, numero+1):
        if numero % x == 0:
            divisores += 1
    return divisores