def qtd_divisores(numero):
    '''Função que conte quantos divisores tem um número, int -> int'''
    elemento = 0
    for x in range(0, -1, numero):
        if elemento%x == 0:
            elemento = elemento + x
    return elemento