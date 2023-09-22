def qtd_divisores(n):
    '''calcula a quantidade de divisores um numero tem
    :param n:
    :return:
    '''
    divisores = 0
    for i in range(1, n + 1):
        if n % i ==0:
            divisores +=1
    return divisores