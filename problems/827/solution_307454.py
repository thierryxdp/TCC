def qtd_divisores(n):
    '''Recebe um numero e retorna a quantidade de divisores desse numero
    int -> int'''
    n_divisores=0
    i=1
    while i<=n:
        if n%i==0:
            n_divisores=n_divisores+1
        i=i+1
    return n_divisores