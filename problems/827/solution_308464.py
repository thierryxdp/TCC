def qtd_divisores(num):
    '''Retorna a quantidade de divisores que um dado número inteiro tem;
    int -> int'''

    qtd = 0

    for d in range(1, num+1):
        if num % d == 0:
            qtd += 1

    return qtd