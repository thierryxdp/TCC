def qtd_divisores(n):
    '''Função que calcula a quantidade total de divisores de um número.
    int -> int'''
    div = 0
    for i in range(1, n + 1):
        if n % i == 0:
            div += 1

    return div