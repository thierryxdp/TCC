def qtd_divisores(n):
    '''função que conta quantos dividores um dado número (n) tem;
    int -> int'''
    divisores = 0
    for i in range(1,n+1):
        if n%i == 0:
            divisores = divisores + 1
    return divisores