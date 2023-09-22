def qtd_divisores(numero):
    '''Função que conte quantos divisores tem um número, int -> int'''
    elemento = 0
    for x in range(numero, 0, -1):
        if numero%elemento == 0:
            numero = numero + 1
    return elemento