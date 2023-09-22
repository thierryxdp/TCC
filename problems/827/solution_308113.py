def qtd_divisores(n):
    '''Conta quantos divisores um número n possui.
int --> int
'''
    cont = 1
    quant_divis = 0
    while cont < (n +1):
        if (n % cont) == 0:
            quant_divis += 1
        cont += 1
    return quant_divis