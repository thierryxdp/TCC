def qtd_divisores(n):
    '''Função que conta quantos divisores um número tem.
    int -> int'''
    x=0
    for elem in range(1,n+1):
        if n%elem==0:
            x = x+1
    return x