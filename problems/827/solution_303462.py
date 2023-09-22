# Quantidade de divisores

def qtd_divisores(num):
    '''Dado um número inteiro, retorna sua quantidade de divsores.
    int -> int'''
    qnt_div = 0
    for x in range(num):
        if num%(x+1) == 0:
            qnt_div += 1
    return qnt_div