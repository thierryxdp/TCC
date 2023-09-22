def qtd_divisores(num):
    '''recebe um inteiro e retorna a quantidade de divisores que este número possui
    int -> int
    '''
    divisores = 0
    for i in range(1, num+1):
        if (num %i == 0):
            divisores += 1
    return divisores