def qtd_divisores(numero):
    '''Conta quantos divisores o numero tem
    int->int'''
    divisores=0
    i=1
    while i<numero:
        if numero/i==int:
            divisores=divisores+1
        i=i+1
    return divisores