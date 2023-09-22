def qtd_divisores(num):
    '''Retorna a quantidade de divisores que um dado número inteiro tem;
    int -> int'''

    qtd = 1

    for d in range(1, num):
        if num % d == 0:
            qtd += 1

    return qtd