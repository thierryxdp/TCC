def qtd_divisores(inteiro):
    '''Conta quantos divisores m dado número inteiro tem
    int -> int'''
    divisores = 0
    for i in range(1, inteiro + 1):
        if inteiro % i == 0:
            divisores += 1
        i += 1
    return divisores