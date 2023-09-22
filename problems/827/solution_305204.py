def qtd_divisores(n):
    '''Retorna a quantidade de divisores inteiros positivos
    do numero n (também inteiro positivo)
    int -> int'''
    n_divisores = 0
    for possibilidades in range(n):
        if n%(possibilidades+1) == 0:
            n_divisores += 1
    return n_divisores