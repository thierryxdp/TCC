def qtd_divisores(n):
    '''Dado um númer, a função retorna quantos divisores o número possui
       int -> int
       Parametros:
       n: número a ser digitado'''
    i = 0
    for c in range (1, n + 1):
        if n % c == 0:
            i += 1
    return i