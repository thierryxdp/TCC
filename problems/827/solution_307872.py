def qtd_divisores(numero):
    '''calcule uma funcao que conte quantos divisores um numero,
    passado como entrada, tem. int-->int.'''
    divisores = 1
    if numero < 0:
        divisores = 0
    for i in range(1, numero):
        if numero%i == 0:
            divisores = divisores + 1
    return divisores