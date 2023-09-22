def colchao(medidas, H, L):
    '''Faça uma função definida, onde medidas é uma lista com os tamanhos inteiros, lista, int, int -> string'''
    if (medidas[1],) <= H*medidas[1] <=L:
        return 'True'
    else:
        return 'False'