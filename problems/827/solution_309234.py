def qtd_divisores(numero):
    '''Função que conte quantos divisores tem um número, int -> int'''
    elemento = 0
    for x in list(range(1, numero + 1)):
        if numero%x == 0:
            elemento = elemento + x
    return elemento