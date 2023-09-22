def qtd_divisores(numero):
    '''Conta quantos divisores um inteiro tem;
       int -> int'''
    divisores = 0
    for divisor in range (1, numero+1):
        if numero%divisor == 0:
            divisores += 1
    return divisores