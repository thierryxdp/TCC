def qtd_divisores(numero):
    '''Função que conte quantos divisores tem um número, int -> int'''
    divisores = 0
    for elemento in numero:
        if elemento%numero == 0:
            divisores = divisores + elemento
    return divisores