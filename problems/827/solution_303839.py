def qtd_divisores(n):
    '''
        Função que retorna a quantidade de divisores de um número.
        Int => Int
    '''
    num_divisores = 0
    for i in range(1, n+1):
        if(n % i == 0):
            num_divisores += 1
    return num_divisores