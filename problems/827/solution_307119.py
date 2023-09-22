def qtd_divisores(numero):
    ''' dado um numero n, retornara a quantidade de divisores desse numero, int > int'''
    divisores = []
    for i in range(1,numero+1):
        if numero%i == 0:
            divisores = divisores+[i,]
    return len(divisores)