def qtd_divisores(numero):
    '''comentario padra
    e1, e2 -> s'''
    num_divisores = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            num_divisores += 1
    return num_divisores