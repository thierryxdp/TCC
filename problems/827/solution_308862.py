def qtd_divisores(numero):
    '''
    dado um numero como argumento, retorna a quantidade
    de divisores que o mesmo possui
    dados de entrada: int
    retorna: int
    '''
    divisores = []
    for i in range(1,numero):
        if (numero % i) == 0:
            list.append(divisores,i)
    return len(divisores)