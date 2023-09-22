def qtd_divisores(numero):
    ''' função que retorna quantidade de divisores existente do número de entrada
    int -> int
    '''
    i = 0
    for elemento in range(1, numero):
        if numero // elemento == 0:
            i += 1
    if numero > 0:
        return i
    else:
        return i + 1