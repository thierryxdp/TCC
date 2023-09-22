def qtd_divisores(num):
    '''retorna a quantidade de divisores que o numero passado possui
    int---->int'''
    soma = 0
    for n in range(num, 0, -1):
        if num % n == 0:
            soma += 1
    return soma