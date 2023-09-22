def qtd_divisores(num):
    '''recebe um inteiro e retorna a quantidade de divisores que este número possui
    int -> int
    '''
    divisores = 0
    i = 1
    while (i <= num):
        if (num %i == 0):
            divisores += 1
        i += 1
    return divisores