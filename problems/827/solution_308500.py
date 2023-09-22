def qtd_divisores(num):
    '''Função que recebe um número e conta quantos
    divisores ele tem.
    int -> int
    '''
    n = 0
    for elemento in range(1,num):
        if num % elemento == 0:
            n += 1

    if num > 0:
        return n + 1
    else:
        return n