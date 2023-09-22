def qtd_divisores(n):
    '''Função que dado um numero n, retorna a quantidade de divisores que esse numero tem:
    int -> int'''
    divisores = 0
    for d in range(1,n+1):
        if n%d == 0:
            divisores = divisores + 1
    return divisores