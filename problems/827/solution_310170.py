def qtd_divisores (numero):
    '''Função que dado um número como entrada, retorna a quantidade
    de divisores que esse número possui
    int -> int'''
    divisores = 0
    for divisor in range(1, numero+1):
        if numero % divisor == 0:
            divisores += 1    
    return divisores