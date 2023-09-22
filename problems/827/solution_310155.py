def qtd_divisores(numero):
    '''Conta quantos divisores um número tem
    entrada:int
    saída:int
    '''
    numerodivisores=0
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            numerodivisores=numerodivisores+1
    return numerodivisores