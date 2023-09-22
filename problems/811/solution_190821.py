def colchao(A, B, C, H, L):
    '''Faça uma função definida, onde medidas é uma lista com os tamanhos inteiros, lista, int, int -> string'''
    if A*B*C:
        return medidas[A,B,C]
    elif medidas[A,B,C] >= H*L:
        return 'True'
    else:
        return 'False'