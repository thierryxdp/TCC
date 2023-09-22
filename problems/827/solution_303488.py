def qtd_divisores(n):
    '''essa função retorna a quantidade de divisores que um numero tem '''
    divisores = list()
    for i in range(1, n+1):
        if n%i == 0:
            divisores.append(i)
    return len(divisores)