def qtd_divisores(x):
    '''funcao que calcula a quantidade de divisores que um
    	numero tem
        x-> int
        return:int
    '''
    divisores = 0
    for i in range(1, x + 1):
        if x % i == 0:
            divisores += 1

    return divisores