def qtd_divisores(numero):
    '''Função que conte quantos divisores tem um número, int -> int'''
    divisores = 0
    for elemento in range(1, n//2+1):
        if numero%elemento == 0:
            return elemento
    return divisores