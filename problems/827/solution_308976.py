def qtd_divisores(numero):
    '''Função que conte quantos divisores tem um número, int -> int'''
    divisores = 0
    for elemento in range(1,numero/2):
        if numero%elemento == 0:
            divisores = divisores + numero
    return divisores