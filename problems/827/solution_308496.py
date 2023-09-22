def qtd_divisores(num):
    '''Função que recebe um número e conta quantos
    divisores ele tem.
    int -> int
    '''
    n = 0
    for el in range(1,num):
        if num % el == 0:
            n = n + 1

    if num < 0:
        return n
    else:
        return n + 1