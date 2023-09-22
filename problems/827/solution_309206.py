def qtd_divisores(numero):
    '''Função que conte quantos divisores tem um número, int -> int'''
    elemento = 0
    for x in range(numero, 0, -1):
        if elemento%x == 0:
            return x
        if elemento == 0:
    return elemento