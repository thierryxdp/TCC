def qtd_divisores(n):
    '''Dado um numero n, retorna a quantidade de divisores que esse numero tem.
    int -> int'''
    contador=0
    for i in range(1,n):
        if n % i == 0:
            contador=contador+1
    return contador